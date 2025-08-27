from pathlib import Path
from conftest import _exists, _read


def test_env_usage_and_examples(cookies, context_defaults):
    result = cookies.bake(extra_context=context_defaults)
    project = Path(result.project_path)

    compose_text = _read(_exists(project, "docker-compose.yml"))
    # ensure Compose references an env file or inline env
    assert (
        ".env" in compose_text
        or "env_file:" in compose_text
        or "environment:" in compose_text
    )

    env_example = project / ".env.example"
    if env_example.exists():
        sample = _read(env_example)
        # basic Django & DB hints if present
        assert "SECRET_KEY" in sample
        assert (
            ("POSTGRES_DB" in sample)
            or ("DATABASE_URL" in sample)
            or ("ALLOWED_HOSTS" in sample)
        )
