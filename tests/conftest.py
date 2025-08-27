from pathlib import Path
# import re
import pytest


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _exists(root: Path, *parts: str) -> Path:
    p = root.joinpath(*parts)
    assert p.exists(), f"Expected {p} to exist"
    return p


def _slugify(name: str) -> str:
    # Mirrors cookiecutter expression:
    # "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}"
    return name.lower().replace(" ", "_").replace("-", "_")


@pytest.fixture
def context_defaults():
    """
    Matches your cookiecutter.json keys exactly.
    Only override what we need for deterministic assertions.
    Leave project_slug to be computed by the template.
    """
    return {
        "project_name": "Example App",
        "project_slug": "example_app",
        # other keys can use their defaults from cookiecutter.json:
        # description, author_name, domain_name, email, timezone, python_version
        "use_nginx": "n",
        "use_postgres": "n",
    }


def assert_no_unrendered_jinja(project_root: Path):
    for p in project_root.rglob("*"):
        if p.is_file():
            body = _read(p)
            assert "{{ cookiecutter" not in body, f"Unrendered variable in {p}"
            assert "{% " not in body and "%}" not in body, f"Unrendered block in {p}"
