# React + Django Boilerplate

Full-stack web application boilerplate with a React frontend and Django backend.

## Quick Start

```bash
# Start both React and Django development servers
./dev-start.sh
```

This will start:

- React development server on http://localhost:3000 
- Django API server on http://localhost:8000

## Project Structure

```
├── frontend/                 
│   ├── src/
│   │   ├── App.jsx          # Main React component
│   │   ├── main.jsx         # React entry point
│   │   ├── App.css          # Component styles
│   │   └── index.css        # Global styles
│   ├── package.json         # Node.js dependencies
│   ├── vite.config.js       # Vite configuration
│   └── index.html           
│
├── backend/                
│   ├── project/             # Django project settings
│   │   ├── settings.py      # Django configuration
│   │   └── urls.py          # URL routing
│   ├── app/                 # Django application
│   │   ├── views.py         # API views
│   │   ├── urls.py          # App URL routing
│   │   └── templates/       # Django templates
│   └── manage.py            # Django CLI
│
├── dev-start.sh             # Development startup script
├── build-and-run.sh         # Production build script
└── README.md                # This file
```

## Dependencies

### Frontend

- **React** - UI library
- **Vite** - Build tool and dev server
- **Axios** - HTTP client for API calls

### Backend

- **Django** - Web framework
- **Django REST Framework** - API development
- **django-cors-headers** - CORS handling

## Next Steps

- Add TailwindCSS
- Set up example database models and migrations
- Deploy this application on a DigitalOcean droplet with nginx