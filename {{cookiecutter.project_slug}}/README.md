# {{cookiecutter.project_name}}

A Django web application scaffolded with Docker Compose.  
Optional profiles for Postgres (`db`) and Nginx (`proxy`).  
Static files served by [WhiteNoise](https://whitenoise.evans.io/) by default.

---

## 🚀 Quickstart

### 1. Requirements
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- (optional, host) Python 3.10+ for tooling

### 2. Initialize
On the first run, use the bootstrap script:

```bash
./init.sh
```

This will:

- Create `.env` (with a generated `SECRET_KEY`) if missing
- Start services with Compose (`dev` profile by default)
- Wait for dependencies (Postgres if enabled)
- Run Django migrations
- Prompt to create a superuser (interactive unless `--noninteractive` / `--superuser` flags are used)

To enable Postgres + Nginx:

```bash
./init.sh --profiles "db proxy"
```

Non-interactive CI-friendly usage:

```bash
./init.sh --noninteractive --profiles "db" --superuser   --su-username admin --su-email admin@example.com --su-password pass123
```

### 3. Makefile shortcuts

Common developer commands are wrapped in a `Makefile`:

```bash
make help        # show all targets
make up          # start stack (default dev profile)
make up-prod     # start prod stack (profiles: prod db proxy)
make down        # stop & remove containers/volumes
make shell       # open shell inside Django container
make migrate     # run migrations
make superuser   # create superuser (interactive)
make test        # run test suite
make fmt lint    # run pre-commit formatting/lint (host)
```

Database helpers (when `db` profile is enabled):

```bash
make dbshell                 # open psql
make db-backup FILE=backup.sql
make db-restore FILE=backup.sql
```

---

## 🔧 Configuration

Environment variables live in `.env` (copied from `.env.example` on init).  
Key variables:

```env
DEBUG=1
SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
# Postgres (if db profile)
POSTGRES_DB=app_db
POSTGRES_USER=app_user
POSTGRES_PASSWORD=app_password
DATABASE_URL=postgres://app_user:app_password@db:5432/app_db
```

---

## 🐳 Services

- **web**: Django + Gunicorn (prod) or runserver (dev)
- **db** (optional, profile `db`): Postgres 16
- **nginx** (optional, profile `proxy`): static/media reverse proxy

Profiles let you tailor stacks:

- `dev` → hot-reload runserver, SQLite default
- `dev db` → Django + Postgres
- `prod db proxy` → Gunicorn + Postgres + Nginx

---

## 🛡️ Healthcheck

Django exposes `/healthz/`:

```bash
curl http://127.0.0.1:8000/healthz/
# → {"status": "ok"}
```

Docker Compose uses this for service health.

---

## 🧪 Development

- Run Django commands inside the container:

  ```bash
  make manage ARGS="createsuperuser"
  make manage ARGS="showmigrations"
  ```

- Run tests:

  ```bash
  make test
  ```

- Format/lint:

  ```bash
  make fmt lint
  ```

Install [pre-commit](https://pre-commit.com/) hooks on host:

```bash
pip install pre-commit
pre-commit install
```

---

## 📦 Deployment

For production:

```bash
make up-prod
```

This will:

- Build with multi-stage Dockerfile
- Run Gunicorn
- Collect static files
- Use Nginx if `proxy` profile enabled

---

## 📝 License

This project is generated from [cc-docker-webapp](https://github.com/homero-s/cc-docker-webapp).  
License: MIT (see upstream).

