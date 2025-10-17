# Multi-stage build: frontends + backend
FROM node:22-alpine AS frontend-builder

WORKDIR /app

# Copy frontend packages
COPY student-frontend/package*.json ./student-frontend/
COPY teacher-frontend/package*.json ./teacher-frontend/

# Build student frontend
WORKDIR /app/student-frontend
RUN npm install
COPY student-frontend/ .
RUN npm run build

# Build teacher frontend
WORKDIR /app/teacher-frontend
RUN npm install
COPY teacher-frontend/ .
RUN npm run build

# Final stage: Python backend
FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend/

# Copy built frontends to backend static/media directories
COPY --from=frontend-builder /app/student-frontend/dist ./backend/static/student-frontend
COPY --from=frontend-builder /app/teacher-frontend/dist ./backend/static/teacher-frontend

# Create necessary directories
RUN mkdir -p /app/backend/staticfiles /app/backend/media

WORKDIR /app/backend

# Expose port (Railway will use $PORT env var)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/api/docs/', timeout=5)" || exit 1

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn eduplatform.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3 --worker-class sync --timeout 120"]
