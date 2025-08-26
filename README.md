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
DATABASE_URL=postgres://user:password@db:5432/app_db
```

---

## 🌐 Optional Nginx Proxy

If you enabled Nginx during setup, it will be included in your `docker-compose.yml` and proxy requests to your Django app automatically.

---

## ✨ Features

- Django 5.2 project scaffold
- Docker Compose setup with Python, Postgres (optional), and Nginx (optional)
- `.env` support out of the box
- Easy extension for production deployments

---

## 📖 Resources

- [Cookiecutter Docs](https://cookiecutter.readthedocs.io/)
- [Django Docs](https://docs.djangoproject.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)

---

✨ That’s it! You now have a fully containerized Django project scaffolded and ready for development.
