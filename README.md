# Cookiecutter Docker Django Template

A Cookiecutter template for quickly creating Django 5.2 web apps with **Docker Compose** and optional **Nginx reverse proxy**.

## Features
- 🐍 Django 5.2 (latest stable)
- 🐳 Dockerfile + docker-compose
- 🌍 Optional Nginx reverse proxy
- 🔧 Environment variables via `.env`
- 🏗 Automatic `django-admin startproject` on first run

## Usage

Install cookiecutter:

```bash
pip install cookiecutter
```

Generate a new project:

```bash
cookiecutter gh:yourusername/cookiecutter-docker-webapp
```

Then:

```bash
cd your_project_slug
docker compose up --build
```

A fresh Django project will appear in `./app/` on your host.
