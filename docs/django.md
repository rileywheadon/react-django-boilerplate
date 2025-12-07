# django

## Installation

1. Install Python
2. Create virtual environment: `python -m venv .venv`
3. Start virtual environment: `source .venv/bin/activate`
4. Install django: `python -m pip install django`
5. Check django version: `django-admin --version`
6. Navigate to project root
7. Bootstrap project: `django-admin startproject project backend`

## Project Setup

### `startproject`

The `startproject` command creates the following files:

```
app/
  manage.py
  backend/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
```

- `settings.py`: https://docs.djangoproject.com/en/6.0/topics/settings/
- `urls.py`: https://docs.djangoproject.com/en/6.0/topics/http/urls/
- `asgi.py`: https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
- `wsgi.py`: https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/

**Note**: The following commands perform administratice tasks in Django:

```
django-admin <command> [options]
manage.py <command> [options]
python -m django <command> [options]
```

- All three options surface the same functionality.
- However, `manage.py` uses the settings for the project in which it exists.

### Development Server

```
python manage.py runserver
```

**Note**: The development server will not automatically reload new files.

## App Setup

**Note**: A Django **Project** is a website, while an **App** is a web application.
A project can contain multiple apps and an app can exist within multiple projects.

To create an app, run the following command:

```
python manage.py startapp app
```

### Views

In Django, a **View** is a URL endpoint that returns an HTTP response.

- Views are defined in `app/views.py`.
- Views must be bound to a URL in `app/views.py`.

The URLs for the app also need a project-level path:

```python
# project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("app/", include("app.urls")),
    path("admin/", admin.site.urls),
]
```

### Default Applications

In `project/settings.py`, the `INSTALLED_APPS` variable provides a list of default Django apps used by the project (see [Database Setup](https://docs.djangoproject.com/en/6.0/intro/tutorial02/#database-setup) for more information).
These can be removed if necessary.

### Templates

- Templates should be stored in `app/templates/app`.
- Adding the second `app` directory **Namespaces** the templates.
- Namespacing allows Django to differentiate between templates in different apps.

After you have created a template, you must add the path to the templates directory to the `TEMPLATES` variable in `project/settings.py`.
You can build file paths in the settings file using the `BASE_DIR` variable.

### Database

TBD

