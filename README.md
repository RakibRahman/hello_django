# hello_django

# Set up project
cd project_root_dir

Set up environment:
```python -m venv env```

Install Django:
```pip install django```

Run Project: ```django-admin startproject project_name```

Run App: ```python manage.py startapp app_name```


Run Server: ```python manage.py runserver``` // active django server on project root path


Migrating Models:
 the three-step guide to making model changes:

Change models (in app/models.py).
Run ```python manage.py makemigrations``` to create migrations for those changes
Run ```python manage.py migrate``` to apply those changes to the database.
