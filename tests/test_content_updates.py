"""Regression tests for automated tutorial and publication updates."""

from pathlib import Path

import pytest

from scripts.update_scholar import ScholarProfileParser, build_scholar_page
from scripts.update_tutorials import ContentUpdateError, replace_directory


def test_tutorial_replacement_requires_a_notebook(tmp_path) -> None:
    """Preserve current tutorials when an upstream copy is incomplete."""
    source_directory = tmp_path / "source"
    destination_directory = tmp_path / "destination"
    source_directory.mkdir()
    destination_directory.mkdir()
    (source_directory / "README.md").write_text("Incomplete", encoding="utf-8")
    current_notebook = destination_directory / "current.ipynb"
    current_notebook.write_text("{}", encoding="utf-8")

    with pytest.raises(ContentUpdateError):
        replace_directory(source_directory, destination_directory)

    assert current_notebook.is_file()


def test_tutorial_replacement_installs_valid_content(tmp_path) -> None:
    """Replace a tutorial track after its notebook content is validated."""
    source_directory = tmp_path / "source"
    destination_directory = tmp_path / "destination"
    source_directory.mkdir()
    destination_directory.mkdir()
    (source_directory / "new.ipynb").write_text("{}", encoding="utf-8")
    (destination_directory / "old.ipynb").write_text("{}", encoding="utf-8")

    replace_directory(source_directory, destination_directory)

    assert (destination_directory / "new.ipynb").is_file()
    assert not (destination_directory / "old.ipynb").exists()


def test_scholar_profile_is_parsed_and_rendered() -> None:
    """Convert Scholar profile fields into the generated publication page."""
    profile_html = """
    <div id="gsc_prf_in">Mathias Louboutin</div>
    <td class="gsc_rsb_std">1909</td>
    <td class="gsc_rsb_std">1500</td>
    <td class="gsc_rsb_std">22</td>
    <td class="gsc_rsb_std">19</td>
    <td class="gsc_rsb_std">39</td>
    <tr class="gsc_a_tr">
      <td class="gsc_a_t">
        <a class="gsc_a_at" href="/citation">Example &amp; result</a>
        <div class="gs_gray">M Louboutin</div>
        <div class="gs_gray">Journal, 2026</div>
      </td>
      <td><a class="gsc_a_ac">12</a></td>
      <td><span class="gsc_a_h">2026</span></td>
    </tr>
    """
    parser = ScholarProfileParser()
    parser.feed(profile_html)
    profile = {
        "profile_name": parser.profile_name,
        "metrics": parser.metrics,
        "articles": parser.articles,
    }

    output = build_scholar_page(profile, "profile-id")

    assert "Example &amp; result" in output
    assert "Cited by 12" in output
    assert "<strong>1909</strong>" in output


def test_update_workflow_includes_all_external_sources() -> None:
    """Keep tutorials, archives, and Scholar in the scheduled refresh."""
    workflow = Path(".github/workflows/update-content.yml").read_text(
        encoding="utf-8"
    )
    expected_commands = [
        "python scripts/update_tutorials.py",
        "julia scripts/mkpubs.jl",
        "python scripts/update_scholar.py",
    ]
    assert all(command in workflow for command in expected_commands)
