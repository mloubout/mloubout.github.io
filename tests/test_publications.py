"""Regression tests for publication archive navigation and external links."""

from pathlib import Path


def get_publication_sources() -> list:
    """Return publication source files that contain DOI links."""
    publication_directory = Path("content/pubs")
    source_names = ["Journals.qmd", "Conferences.qmd", "TechReports.qmd"]
    return [publication_directory / name for name in source_names]


def test_doi_links_are_absolute() -> None:
    """Ensure DOI buttons cannot be interpreted as local site paths."""
    for source_path in get_publication_sources():
        source_text = source_path.read_text(encoding="utf-8")
        assert "](doi.org/" not in source_text
        assert "https://doi.org/https://" not in source_text


def test_publication_archive_uses_navbar_menu() -> None:
    """Ensure publication categories remain accessible from the main navbar."""
    configuration = Path("_quarto.yml").read_text(encoding="utf-8")
    expected_labels = [
        "Journal articles",
        "Conference papers",
        "Presentations",
        "Technical reports",
        "Google Scholar",
    ]
    assert all(label in configuration for label in expected_labels)
