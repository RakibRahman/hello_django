# hello_django


# Install Django:
```pip install django```

# Set up project
- Set up virtual environment: ```python -m venv env```, cd project_root_dir
- Run Project: ```django-admin startproject project_name```
- Run App: ```python manage.py startapp app_name```
- Run Server: ```python manage.py runserver``` // active Django server on project root path


# Migrating Models:
### The three-step guide to making model changes:

- Change models (in app/models.py).
- Run ```python manage.py makemigrations``` to create migrations for those changes
- Run ```python manage.py migrate``` to apply those changes to the database.
