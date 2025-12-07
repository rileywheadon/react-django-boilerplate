## API Integration

The React app is configured to communicate with Django APIs:

- **Development**: Vite proxy forwards `/api/*` requests to Django (localhost:8000)
- **Production**: React build is served by Django as static files

### Example API Call

```javascript
// In React components
const response = await axios.get('/api/hello/');
console.log(response.data.message); // "Hello from Django API!"
```

### Django API Endpoint

```python
# In backend/app/views.py
@api_view(['GET'])
def hello_api(request):
    return Response({
        'message': 'Hello from Django API!',
        'status': 'success'
    })
```

## Configuration

### Vite Configuration (`frontend/vite.config.js`)
- Proxy configuration for API calls during development
- Build output directed to Django static folder
- Hot module replacement enabled

### Django Configuration (`backend/project/settings.py`)
- CORS headers configured for React development server
- REST Framework configured with permissive settings
- Static files configured to serve React build

