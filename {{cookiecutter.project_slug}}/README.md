# {{cookiecutter.project_name}}

Generated with [Cookiecutter](https://github.com/cookiecutter/cookiecutter).

## 🚀 Quick Start

```bash
docker compose up --build
```

- Django app: [http://localhost:8000](http://localhost:8000)  
{% if cookiecutter.use_nginx == "y" %}
- With Nginx proxy: [http://localhost](http://localhost)
{% endif %}

## 📝 Notes
- On first run, a new **Django 5.2** project (`{{cookiecutter.project_slug}}`) will be generated automatically inside `./app`.
- On later runs, the existing project will be reused (not overwritten).
- You can edit `app/` directly on your host machine — changes are live in the container.
