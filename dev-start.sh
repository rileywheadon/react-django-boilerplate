#!/bin/bash

# Development Script for React and Django 

set -xe -o pipefail

: ::: Starting React + Django Development Environment

# Function to handle cleanup
cleanup() {
    : ::: "Shutting down servers..."
    kill $REACT_PID $DJANGO_PID 2> /dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Start Django development server
: ::: Starting Django development server on http://localhost:8000...
cd backend
python manage.py runserver > /dev/null 2>&1 &
DJANGO_PID=$!

# Start React development server
: ::: Starting React development server on http://localhost:3000...
cd ../frontend
npm run dev > /dev/null 2>&1 &
REACT_PID=$!

: ::: Both servers are running...
: ::: React App: http://localhost:3000
: ::: Django API: http://localhost:8000
: ::: Press Ctrl+C to stop both servers

# Wait for both processes
wait $REACT_PID $DJANGO_PID