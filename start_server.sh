#!/bin/bash

echo "Starting Backend..."
cd /home/deepak/srideep/backend
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000 &
BACKEND_PID=$!

echo "Starting Frontend..."
cd /home/deepak/srideep/frontend/srideep-frontend
npm start &
FRONTEND_PID=$!

echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"

wait
