#!/bin/bash
# Railway build and start script
# This script is executed by Railway when Dockerfile is not used

set -e

echo "=========================================="
echo "Railway Start Script - Multi-Service Build"
echo "=========================================="

# Change to backend directory
cd backend

echo ""
echo "1️⃣ Installing Python dependencies..."
pip install --no-cache-dir -r requirements.txt

echo ""
echo "2️⃣ Running Django migrations..."
python manage.py migrate --noinput

echo ""
echo "3️⃣ Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "4️⃣ Starting Django server..."
gunicorn eduplatform.wsgi:application \
  --bind 0.0.0.0:${PORT:-8000} \
  --workers 3 \
  --worker-class sync \
  --timeout 120 \
  --access-logfile - \
  --error-logfile -
