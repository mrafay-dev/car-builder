#!/bin/bash
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Build frontend first
cd frontend
npm install
npm run build
cd ..

# Collect static files (includes React assets)
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate
