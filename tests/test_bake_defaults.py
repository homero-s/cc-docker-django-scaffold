from pathlib import Path
from conftest import _exists, _read, assert_no_unrendered_jinja


def test_bake_with_defaults(cookies, context_defaults):
    result = cookies.bake(extra_context=context_defaults)
    assert result.exit_code == 0, result.exception
    assert result.exception is None

    project = Path(result.project_path)
    assert project.name == context_defaults["project_slug"]

    # Core files the README promises
    # Dockerfile + docker-compose.yml should be at template root
    dockerfile = _exists(project, "Dockerfile")
    compose = _exists(project, "docker-compose.yml")

    # Basic sanity: Dockerfile mentions a Python base (Django app)
    text = _read(dockerfile).lower()
    assert "from" in text and "python" in text

    # Compose must define a web service; db/nginx are optional by defaults
    compose_text = _read(compose)
    assert "services:" in compose_text
    assert "web:" in compose_text

    # Defaults select SQLite: no Postgres service should be present
    assert "postgres" not in compose_text.lower()
    assert (
        "db:" not in compose_text.splitlines()
    ), "Unexpected db service for SQLite default"

    # Nginx disabled by default per our defaults
    assert "nginx:" not in compose_text

    # README should render and contain quickstart hints mentioned in your repo
    readme = _read(_exists(project, "README.md")).lower()
    assert "cookiecutter" in readme or "docker compose" in readme

    # No leftover Jinja
    assert_no_unrendered_jinja(project)
