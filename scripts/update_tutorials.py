"""Synchronize tutorial content from the upstream Devito and JUDI projects."""

import argparse
import logging
import shutil
import subprocess
import tempfile
from pathlib import Path


class ContentUpdateError(RuntimeError):
    """Raised when upstream tutorial content cannot be updated safely."""


def run_command(command: list, working_directory=None) -> None:
    """Run a command and raise a focused error when it fails."""
    try:
        subprocess.run(
            command,
            cwd=working_directory,
            check=True,
            text=True,
        )
    except subprocess.CalledProcessError as error:
        command_text = " ".join(command)
        raise ContentUpdateError(
            f"Tutorial update command failed: {command_text}"
        ) from error


def clone_sparse_repository(
    repository_url: str,
    branch: str,
    source_paths: list,
    destination_directory,
) -> None:
    """Clone only the upstream directories needed by the website."""
    run_command(
        [
            "git",
            "clone",
            "--depth=1",
            "--filter=blob:none",
            "--sparse",
            "--branch",
            branch,
            repository_url,
            str(destination_directory),
        ]
    )
    run_command(
        ["git", "sparse-checkout", "set", *source_paths],
        working_directory=destination_directory,
    )


def validate_tutorial_directory(source_directory) -> None:
    """Reject incomplete upstream content before replacing local files."""
    if not source_directory.is_dir():
        raise ContentUpdateError(
            f"Expected upstream directory is missing: {source_directory}"
        )
    notebooks = list(source_directory.glob("*.ipynb"))
    if not notebooks:
        raise ContentUpdateError(
            f"No notebooks found in upstream directory: {source_directory}"
        )


def replace_directory(source_directory, destination_directory) -> None:
    """Replace one tutorial directory only after staging a complete copy."""
    validate_tutorial_directory(source_directory)
    destination_parent = destination_directory.parent
    destination_parent.mkdir(parents=True, exist_ok=True)
    backup_directory = destination_parent / (
        f".{destination_directory.name}.update-backup"
    )
    if backup_directory.exists():
        raise ContentUpdateError(
            f"Remove stale update backup before continuing: {backup_directory}"
        )

    with tempfile.TemporaryDirectory(
        prefix=f".{destination_directory.name}.update-",
        dir=destination_parent,
    ) as temporary_path:
        staged_directory = Path(temporary_path) / destination_directory.name
        shutil.copytree(source_directory, staged_directory)
        try:
            if destination_directory.exists():
                destination_directory.rename(backup_directory)
            staged_directory.rename(destination_directory)
        except OSError as error:
            if (
                backup_directory.exists()
                and not destination_directory.exists()
            ):
                backup_directory.rename(destination_directory)
            raise ContentUpdateError(
                "Could not replace tutorial directory: "
                f"{destination_directory}"
            ) from error

    if backup_directory.exists():
        shutil.rmtree(backup_directory)


def update_tutorials(project_root: str) -> None:
    """Fetch and install current upstream tutorial directories."""
    root_path = Path(project_root).resolve()
    tutorial_directory = root_path / "content" / "tutorials"
    repository_specs = [
        {
            "name": "devito",
            "url": "https://github.com/devitocodes/devito.git",
            "branch": "main",
            "paths": ["examples/userapi", "examples/seismic/tutorials"],
            "mappings": [
                ("examples/userapi", "devitoapi"),
                ("examples/seismic/tutorials", "devitotutos"),
            ],
        },
        {
            "name": "judi",
            "url": "https://github.com/slimgroup/JUDI.jl.git",
            "branch": "master",
            "paths": ["examples/notebooks"],
            "mappings": [("examples/notebooks", "judituto")],
        },
    ]

    with tempfile.TemporaryDirectory(prefix="tutorial-update-") as temp_path:
        temporary_root = Path(temp_path)
        for repository in repository_specs:
            clone_directory = temporary_root / repository["name"]
            logging.info("Fetching tutorials from %s", repository["url"])
            clone_sparse_repository(
                repository["url"],
                repository["branch"],
                repository["paths"],
                clone_directory,
            )
            for source_path, destination_name in repository["mappings"]:
                replace_directory(
                    clone_directory / source_path,
                    tutorial_directory / destination_name,
                )


def main() -> None:
    """Parse command-line arguments and update tutorial content."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Website repository root.",
    )
    arguments = parser.parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    update_tutorials(arguments.project_root)


if __name__ == "__main__":
    main()
