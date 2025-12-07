#!/bin/bash

# Build and Deploy Script for React + Django

set -ex -o pipefail

: ::: Deploying React + Django Application

# Function to handle cleanup
cleanup() {
    : ::: "Shutting down servers..."
    kill $DJANGO_PID 2> /dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

: ::: Building React frontend...
cd frontend
npm run build > /dev/null 2>&1

: ::: Setting up Django backend...
cd ../backend
python manage.py runserver # > /dev/null 2>&1 &
DJANGO_PID=$!

: ::: Setup complete! Your app should be running at http://localhost:8000

# Wait for Django server to exit
wait $DJANGO_PID