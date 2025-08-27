import pytest
from pathlib import Path
from conftest import _exists, _read


@pytest.mark.parametrize("use_postgres", ["y", "n"])
@pytest.mark.parametrize("use_nginx", ["y", "n"])
def test_matrix_postgres_and_nginx(cookies, context_defaults, use_postgres, use_nginx):
    ctx = dict(context_defaults)
    ctx["use_postgres"] = use_postgres
    ctx["use_nginx"] = use_nginx

    result = cookies.bake(extra_context=ctx)
    assert result.exit_code == 0, result.exception
    project = Path(result.project_path)

    compose_text = _read(_exists(project, "docker-compose.yml"))

    # web must always be present
    assert "web:" in compose_text

    # Postgres toggle controls DB service presence
    if use_postgres == "y":
        assert ("db:" in compose_text) or ("postgres" in compose_text.lower())
        # look for typical envs when Postgres is enabled
        assert any(
            k in compose_text
            for k in [
                "POSTGRES_DB",
                "POSTGRES_USER",
                "POSTGRES_PASSWORD",
                "DATABASE_URL",
            ]
        )
    else:
        assert "db:" not in compose_text
        assert "postgres" not in compose_text.lower()

    # Nginx toggle
    if use_nginx == "y":
        assert "nginx:" in compose_text
        # a port mapping commonly used for reverse proxy
        assert (":80" in compose_text) or (":8080" in compose_text)
    else:
        assert "nginx:" not in compose_text
