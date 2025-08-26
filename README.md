# 🐳 cc-docker-webapp

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for quickly bootstrapping a **Django 5.2** web application with **Docker Compose** and optional **Nginx** reverse proxy support.

This template sets up a containerized Django project with sensible defaults so you can focus on building your app instead of boilerplate.

---

## 🚀 Generate a New Project

First, make sure you have **Python 3.10+** and **pip** installed. Then install [Cookiecutter](https://cookiecutter.readthedocs.io/):

```bash
pip install cookiecutter
```

Now generate a new project from this template:

```bash
cookiecutter https://github.com/homero-s/cc-docker-webapp
```

Cookiecutter will prompt you for some details (project name, slug, database, Nginx option, etc.).  
Default values are provided in [`cookiecutter.json`](./cookiecutter.json).

---

## 🐳 Running the Project with Docker

Once your project is created:

```bash
cd <your_project_slug>
docker compose up --build
```

This will spin up your Django app (and database / Nginx if you enabled them).

---

## ⚙️ Database Options

When you generate a project, you can choose which database backend to use:

- **SQLite** (default): Lightweight and great for quick prototypes or local development.  
- **Postgres**: A production-ready relational database. This template includes a ready-to-run Postgres container in `docker-compose.yml`.

If you select **Postgres**, update your `.env` file with the correct connection string **and** Postgres credentials:

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

## ⚙️ Common Management Commands

Run Django commands inside the `web` container:

```bash
# Apply database migrations
docker compose exec web python manage.py migrate

# Create a Django superuser
docker compose exec web python manage.py createsuperuser

# Run tests
docker compose exec web python manage.py test
```

---

## 📂 Environment Variables

Put your environment configuration in a `.env` file at the root of your project. Docker Compose will automatically load it.

Example:

```env
DEBUG=1
SECRET_KEY=supersecret
# For Postgres projects (recommended for dev/prod):
DATABASE_URL=postgres://app_user:app_password@db:5432/app_db
POSTGRES_DB=app_db
POSTGRES_USER=app_user
POSTGRES_PASSWORD=app_password
# For SQLite projects (no DATABASE_URL needed)
```

---

## 🌐 Optional Nginx Proxy

If you enabled Nginx during setup, it will be included in your `docker-compose.yml` and proxy requests to your Django app automatically.

---

## ✨ Features

- Django 5.2 project scaffold
- Docker Compose setup with Python, Postgres (optional), and Nginx (optional)
- `.env` support out of the box
- Supports **SQLite** (default) and **Postgres** databases
- Easy extension for production deployments

---

## 🔧 How Postgres is wired

- `docker-compose.yml` defines a `db` service using the official **postgres:16** image.
- On first start, Postgres reads environment variables from `.env` to initialize the database.
- Optional SQL scripts in `db/init/` are automatically run by the container (e.g., to create extensions).

---

## 📖 Resources

- [Cookiecutter Docs](https://cookiecutter.readthedocs.io/)
- [Django Docs](https://docs.djangoproject.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)

---

✨ That’s it! You now have a fully containerized Django project scaffolded and ready for development.
