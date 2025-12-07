# Deployment Plan

This document outlines the process to deploy this React/Django application on a single DigitalOcean droplet.
We will use:

- uvicorn (an ASGI application server)
- nginx (reverse proxy and static file server)
- sqlite3 (database)

## Outline of Deployment Steps 

### 1: Provision the Droplet

- Create a DigitalOcean droplet running Ubuntu.
- Create a non-root user for deploying the application.
- Ensure that SSH is working and secure.

### 2: Install System Packages

- Python (pip, virtualenv)
- nginx
- certbot
- git

### 3: Install Dependencies

Clone the repository, create and activate a virtual environment, run: 

```
pip install -r requirements.txt
```

### 4: Configure Production Environment 

Production must use secure and correct [settings](https://docs.djangoproject.com/en/5.2/topics/settings/):

- Make use of a `.env` file to store sensitive data (like `SECRET_KEY`).
- Ensure that `DEBUG=False` and `ALLOWED_HOSTS` are configured properly.
- Ensure that `STATIC_ROOT` is set for the Django `collectstatic` command.

### 5: Collect Static Files

Django's `collectstatic` command gathers all static assets into a single directory that nginx can serve directly.
Serving static files from nginx is more efficient than via Python.
To collect static files, run:

```
python manage.py collectstatic --noinput
```

This will populate the `STATIC_ROOT` directory (configured in the Django settings) on the disk.
Configure nginx to serve this directory at `/static/`.

### 6: Run Database Migrations

Ensure that `DATABASES` are configured properly in Django settings.

Run `python manage.py migrate` to apply all database migrations.

### 7: Run uvicorn with systemd

systemd provides process supervision (restart on crash, start on boot) and reduces permission scope.
With this design, nginx proxies to a unix socket and never exposes the Python process directly ot the network.

Create a systemd service file that runs uvicorn with the project’s ASGI app object and binds to a unix socket (for example `/run/react_django_boilerplate.sock`). 
Ensure the socket file is created with permissions that allow nginx's `www-data` user to access it (or use a group that both the uvicorn process and nginx share).

### 8: Configure nginx 

Create an nginx site block that:

- Serves `/static/` directly from the `STATIC_ROOT` path.
- Proxies other requests to the unix socket or localhost port where uvicorn listens.
- Sets proxy headers (Host, X-Real-IP, X-Forwarded-For, X-Forwarded-Proto).
- Enforces client body size limits and timeouts suitable for your app.

### 9: Obtain TLS Certificates

Use certbot to request a certificate and configure nginx to serve 443. 
Certbot can auto-update nginx configs and set up a renewal cron or systemd timer.

### 10: Backups 

Schedule database dumps using cron to our local machine.

### 11: Deploy Workflow 

Deployments should be repeatable and predictable.
The simplest approach is to SSH into the droplet and run the following commands:

```
git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
systemctl restart myapp
```

Ideally, we can put these commands into [GitHub Action](https://github.com/appleboy/ssh-action) that runs every time a new commit is pushed to the master branch of our repository.


