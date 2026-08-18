"""Regression tests for the redesigned portfolio section pages."""

from pathlib import Path


def test_tutorial_entry_points_exist() -> None:
    """Ensure each tutorial track starts at an available notebook."""
    tutorial_source = Path("content/tutorials/tutorials.qmd").read_text(
        encoding="utf-8"
    )
    entry_points = [
        ("devitoapi/00_sympy.html", "devitoapi/00_sympy.ipynb"),
        ("devitotutos/01_modelling.html", "devitotutos/01_modelling.ipynb"),
        ("judituto/01_intro.html", "judituto/01_intro.ipynb"),
    ]
    for rendered_link, notebook_path in entry_points:
        assert rendered_link in tutorial_source
        assert (Path("content/tutorials") / notebook_path).is_file()


def test_resume_download_exists() -> None:
    """Ensure the résumé download button points to an available PDF."""
    resume_source = Path("content/resume.qmd").read_text(encoding="utf-8")
    assert "resume/cv/resume.pdf" in resume_source
    assert Path("content/resume/cv/resume.pdf").is_file()


def test_featured_software_links_are_present() -> None:
    """Ensure the primary software projects retain direct repository links."""
    software_source = Path("content/software/software.qmd").read_text(
        encoding="utf-8"
    )
    expected_repositories = [
        "https://github.com/devitocodes/devito",
        "https://github.com/slimgroup/JUDI.jl",
    ]
    assert all(link in software_source for link in expected_repositories)
