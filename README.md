# cc-docker-django-scaffold

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for quickly bootstrapping a **Docker Compose** project scaffold. It will allow you to create a  **Django** web application with **Database** support for SQLite and Postgres, and optional **Nginx** reverse proxy support.

This template sets up a containerized Django project with sensible defaults so you can focus on building your app instead of boilerplate.

---

## 🚀 Generate a New Project

Personally I enjoy using [pipenv](https://pipenv.pypa.io/en/latest/).


First, make sure you have a virtualenv set up with at least **Python 3.10+**. Then install [Cookiecutter](https://cookiecutter.readthedocs.io/):

```bash
pipenv --python 3.10
pipenv shell 
pipenv install -r requirements-dev.txt
```

Now generate a new project from this template:

```bash
cookiecutter gh:homero-s/cc-docker-webapp
```

Cookiecutter will prompt you for some details (project name, slug, database, Nginx option, etc.).  
Default values are provided in [`cookiecutter.json`](./cookiecutter.json).

---

### 🗄️ Database Options

When you generate a project, you can choose which database backend to use:

- **SQLite**: Lightweight and great for quick prototypes or local development.  
- **Postgres** (default): A production-ready relational database. This template includes a ready-to-run Postgres container in `docker-compose.yml`.

If you select **Postgres**, update your `.env.example` file with the correct connection string **and** Postgres credentials:

```env
# DATABASE_URL takes precedence if set
DATABASE_URL=postgres://app_user:app_password@db:5432/app_db

# These are used by the `db` service (Postgres container)
POSTGRES_DB=app_db
POSTGRES_USER=app_user
POSTGRES_PASSWORD=app_password
```

If you use **SQLite**, Django will automatically use a local `db.sqlite3` file inside the container.

---

## 🐳 Running the Project with Docker

Read setup instructions in the generated project files `{{cookiecutter.project_slug}}/README.md`
Put your environment configuration in `.env.example` file at the root of your project. 

---

## ✨ Features

- Django project scaffold
- Docker Compose setup with Python, Postgres (optional), and Nginx (optional)
- Easily extensible

---

## 🧪Test Suite

This template includes a ready-made **pytest test suite** powered by [pytest-cookies](https://github.com/hackebrot/pytest-cookies).  
It automatically bakes the template with different options (`use_postgres`, `use_nginx`) and checks that the generated project is valid.

### Install dependencies

If you’re using **requirements file**:

```bash
pip install -r requirements-dev.txt
```


### Run tests

Run all tests:

```bash
pytest
```

Run with less output:

```bash
pytest -q
```

Run a specific test file:

```bash
pytest tests/test_bake_defaults.py -v
```

### What the tests cover

- ✅ **Bake with defaults** (SQLite + no Nginx)  
- ✅ **Option matrix** (`use_postgres=y/n`, `use_nginx=y/n`)  
- ✅ **File integrity**: no unrendered Jinja, `.env` usage, core files exist  


---

## 📖 Resources

- [Cookiecutter Docs](https://cookiecutter.readthedocs.io/)
- [Django Docs](https://docs.djangoproject.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)

---
