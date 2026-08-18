"""Create a local publication snapshot from a public Google Scholar profile."""

import argparse
import html
import logging
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen


class ScholarUpdateError(RuntimeError):
    """Raised when a Google Scholar snapshot cannot be updated safely."""


class ScholarProfileParser(HTMLParser):
    """Parse article rows and summary metrics from a Scholar profile page."""

    def __init__(self) -> None:
        """Initialize parser state for one profile page."""
        super().__init__()
        self.articles = []
        self.metrics = []
        self.profile_name = ""
        self.current_article = None
        self.capture_field = ""
        self.capture_tag = ""
        self.capture_parts = []

    def handle_starttag(self, tag: str, attributes: list) -> None:
        """Start capturing fields identified by Scholar CSS classes."""
        attribute_map = dict(attributes)
        classes = set(attribute_map.get("class", "").split())
        if tag == "tr" and "gsc_a_tr" in classes:
            self.current_article = {
                "title": "",
                "link": "",
                "details": [],
                "citations": "0",
                "year": "",
            }
        if "gsc_rsb_std" in classes:
            self._start_capture("metric", tag)
        elif attribute_map.get("id") == "gsc_prf_in":
            self._start_capture("profile_name", tag)
        elif self.current_article is not None and "gsc_a_at" in classes:
            self.current_article["link"] = urljoin(
                "https://scholar.google.com",
                attribute_map.get("href", ""),
            )
            self._start_capture("title", tag)
        elif self.current_article is not None and "gs_gray" in classes:
            self._start_capture("detail", tag)
        elif self.current_article is not None and "gsc_a_ac" in classes:
            self._start_capture("citations", tag)
        elif self.current_article is not None and "gsc_a_h" in classes:
            self._start_capture("year", tag)

    def handle_data(self, data: str) -> None:
        """Collect text while a relevant element is active."""
        if self.capture_field:
            self.capture_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        """Finish captured fields and complete article rows."""
        if self.capture_field and tag == self.capture_tag:
            value = " ".join("".join(self.capture_parts).split())
            self._store_capture(value)
            self.capture_field = ""
            self.capture_tag = ""
            self.capture_parts = []
        if tag == "tr" and self.current_article is not None:
            if self.current_article["title"]:
                self.articles.append(self.current_article)
            self.current_article = None

    def _start_capture(self, field_name: str, tag: str) -> None:
        """Begin collecting the text of one Scholar field."""
        self.capture_field = field_name
        self.capture_tag = tag
        self.capture_parts = []

    def _store_capture(self, value: str) -> None:
        """Store a completed field in the current profile or article."""
        if self.capture_field == "metric":
            self.metrics.append(value)
        elif self.capture_field == "profile_name":
            self.profile_name = value
        elif self.current_article is None:
            return
        elif self.capture_field == "detail":
            self.current_article["details"].append(value)
        else:
            self.current_article[self.capture_field] = value


def fetch_profile_page(profile_id: str, start: int, page_size: int) -> str:
    """Fetch one public Scholar profile page without mutating local content."""
    parameters = urlencode(
        {
            "user": profile_id,
            "hl": "en",
            "cstart": start,
            "pagesize": page_size,
            "sortby": "pubdate",
        }
    )
    request = Request(
        "https://scholar.google.com/citations?" + parameters,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (compatible; personal-site-publication-sync/1.0)"
            )
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8", errors="replace")
    except (HTTPError, URLError, TimeoutError) as error:
        raise ScholarUpdateError(
            "Google Scholar did not return the public author profile."
        ) from error


def fetch_profile(profile_id: str) -> dict:
    """Fetch visible articles and profile metrics for one Scholar author."""
    page_size = 100
    articles = []
    metrics = []
    profile_name = ""
    for start in range(0, 1000, page_size):
        parser = ScholarProfileParser()
        parser.feed(fetch_profile_page(profile_id, start, page_size))
        if start == 0:
            metrics = parser.metrics
            profile_name = parser.profile_name
        articles.extend(parser.articles)
        if len(parser.articles) < page_size:
            break

    if not profile_name or not articles:
        raise ScholarUpdateError(
            "Scholar response did not contain a valid public author profile."
        )
    return {
        "profile_name": profile_name,
        "metrics": metrics,
        "articles": articles,
    }


def metric_value(metrics: list, index: int) -> str:
    """Return one summary metric or a safe placeholder."""
    return metrics[index] if len(metrics) > index else "—"


def build_scholar_page(profile: dict, profile_id: str) -> str:
    """Render a Quarto page containing current Scholar metrics and articles."""
    metrics = profile["metrics"]
    profile_url = (
        "https://scholar.google.com/citations?"
        f"user={profile_id}&hl=en&sortby=pubdate"
    )
    lines = [
        "---",
        'title: "Google Scholar"',
        'subtitle: "Current citation profile and publication index"',
        "toc: true",
        "toc-depth: 1",
        "body-classes: publication-list-page scholar-page",
        "---",
        "",
        "::: {.publication-intro}",
        "This snapshot is refreshed from my public Google Scholar profile.",
        "The curated publication categories remain available from the main",
        "Publications menu.",
        "",
        f"[Open the live Google Scholar profile]({profile_url})",
        ":::",
        "",
        "::: {.scholar-metrics}",
        "::: {.scholar-metric}",
        f'<strong>{html.escape(metric_value(metrics, 0))}</strong>',
        "<span>Total citations</span>",
        ":::",
        "::: {.scholar-metric}",
        f'<strong>{html.escape(metric_value(metrics, 2))}</strong>',
        "<span>h-index</span>",
        ":::",
        "::: {.scholar-metric}",
        f'<strong>{html.escape(metric_value(metrics, 4))}</strong>',
        "<span>i10-index</span>",
        ":::",
        ":::",
        "",
        "# Publications",
        "",
    ]
    for article in profile["articles"]:
        title = html.escape(article["title"])
        link = html.escape(article["link"], quote=True)
        details = [html.escape(value) for value in article["details"] if value]
        year = html.escape(article["year"] or "Year unavailable")
        citations = html.escape(article["citations"] or "0")
        lines.extend(
            [
                f'## <a href="{link}">{title}</a>',
                "",
                " · ".join(details),
                "",
                f"{year} · Cited by {citations}",
                "",
            ]
        )
    return "\n".join(lines)


def update_scholar(project_root: str, profile_id: str) -> None:
    """Fetch Scholar data and replace the generated page after validation."""
    profile = fetch_profile(profile_id)
    output_path = (
        Path(project_root).resolve() / "content" / "pubs" / "Scholar.qmd"
    )
    output_text = build_scholar_page(profile, profile_id)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=output_path.parent,
        delete=False,
    ) as temporary_file:
        temporary_file.write(output_text)
        temporary_path = Path(temporary_file.name)
    temporary_path.replace(output_path)
    logging.info(
        "Updated Google Scholar snapshot with %s articles",
        len(profile["articles"]),
    )


def main() -> None:
    """Parse command-line arguments and refresh the Scholar page."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Website repository root.",
    )
    parser.add_argument(
        "--profile-id",
        default="RGVC664AAAAJ",
        help="Public Google Scholar author ID.",
    )
    arguments = parser.parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    update_scholar(arguments.project_root, arguments.profile_id)


if __name__ == "__main__":
    main()
