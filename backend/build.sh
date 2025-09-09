#!/bin/bash
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Move to the frontend folder one level up
cd ../frontend
npm install
npm run build
cd ../backend

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate
