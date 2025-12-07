# react

## Architecture

### Development Mode

- **React Dev Server**: Runs on `localhost:3000` with hot module replacement
- **Proxy Configuration**: Vite proxies `/api/*` requests to Django during development

### Production Mode

- **Static Build**: React is compiled to static assets with hashed filenames
- **Single Server**: Everything runs on Django's port (`localhost:8000`)

## Project Structure

```
frontend/
├── package.json         # Dependencies and build scripts
├── vite.config.js       # Vite configuration
├── index.html           # HTML entry point
└── src/
    ├── main.jsx         # React application entry point
    ├── App.jsx          # Main App component
    ├── App.css          # App-specific styles
    └── index.css        # Global styles
```

## API Integration

The React app is configured to communicate with Django APIs:

- **Development**: Vite proxy forwards `/api/*` requests to Django (localhost:8000)
- **Production**: React build is served by Django as static files

We use [Axios](https://axios-http.com/) to make HTTP requests.

### Example API Call

```javascript
// In React components
const response = await axios.get('/api/hello/');
console.log(response.data.message); // "Hello from Django API!"
```


