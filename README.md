# React + Django Boilerplate

Full-stack web application boilerplate with a React frontend and Django backend.

## Quick Start

### Development Mode

```bash
# Start both React and Django development servers
./dev-start.sh
```

This will start:

- React development server on http://localhost:3000 (with hot reloading)
- Django API server on http://localhost:8000

### Production Mode

```bash
# Build React and serve through Django
./build-and-run.sh
```

This will build the React app and serve it through Django on http://localhost:8000

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

- Debug why the `./build-and-run.sh` script is not working.

---

- Add authentication (JWT tokens)
- Set up database models and migrations
- Add React routing with React Router
- Implement form handling and validation
- Add tests for both frontend and backend
- Set up CI/CD pipeline