# Railway Build Configuration Guide

## Overview

Your project has been configured for seamless deployment on Railway with:
- **Dockerfile** for multi-stage builds (Node.js frontends → Python backend)
- **start.sh** as fallback script
- **railway.toml** with optimized settings
- **.dockerignore** & **.railwayignore** for build optimization

---

## Build Flow

### Stage 1: Frontend Build (Node.js)
```
1. Install student-frontend dependencies (npm install)
2. Build student-frontend (npm run build → dist/)
3. Install teacher-frontend dependencies (npm install)
4. Build teacher-frontend (npm run build → dist/)
```

### Stage 2: Backend Deployment (Python)
```
5. Install backend dependencies (pip install requirements.txt)
6. Copy built frontends to backend/static/
7. Run migrations (python manage.py migrate)
8. Collect static files (python manage.py collectstatic)
9. Start gunicorn server (port 8000)
```

---

## Files Created/Updated

### 📄 Dockerfile
- Multi-stage build for Node.js + Python
- Builds both frontends, bundles static files
- Runs migrations automatically
- Starts gunicorn on Railway's $PORT

### 📄 start.sh
- Bash script fallback (if Dockerfile not detected)
- Runs same steps as Dockerfile
- Used by older Railway deployments

### 📄 railway.toml
- Specifies Dockerfile builder
- Configures health checks
- Sets resource limits (1GB memory, 0.5 CPU)
- Configures restart policy

### 📄 .dockerignore
- Excludes unnecessary files from Docker build
- Reduces image size
- Speeds up build process

### 📄 .railwayignore
- Tells Railway what to ignore during deployment
- Prevents redundant files from being sent

### 📄 .buildpacks
- Alternative build detection (Heroku-compatible)
- Fallback if Dockerfile not recognized

### 📄 docker-compose.yml
- Local Docker Compose for testing
- Includes PostgreSQL database
- Mirrors Railway environment locally

---

## Environment Variables (Set in Railway)

Ensure these are set in your Railway project:

```
DEBUG=False                    # Set to False for production
SECRET_KEY=<your-secret-key>  # Use a strong random key
DATABASE_URL=<your-db-url>    # Railway sets this automatically
ALLOWED_HOSTS=your-domain.railway.app,www.your-domain.railway.app
CORS_ALLOWED_ORIGINS=<frontend-urls>
```

---

## Deployment Process

### Step 1: Push to Git
```bash
git add .
git commit -m "Add Railway build configuration"
git push
```

### Step 2: Deploy via Railway CLI
```powershell
railway link -p b64abf5f-0974-4a4e-a9a5-329b921e000f
railway up
```

### Step 3: Monitor Build
```powershell
railway logs -f
```

Expected output:
```
1️⃣ Installing Python dependencies...
2️⃣ Running Django migrations...
3️⃣ Collecting static files...
4️⃣ Starting Django server...
Listening on 0.0.0.0:8000
```

---

## Build Optimization

### Image Size
- Multi-stage build: ~200MB (final image)
- Node.js stage discarded after build
- Only Python + Django included in final image

### Build Time
- Estimated: 3-5 minutes (first build)
- Subsequent builds: 1-2 minutes (cached layers)

### Caching
- Node modules cached per frontend
- Python packages cached
- Docker layers cached when no changes

---

## Troubleshooting

### "Dockerfile not found"
✅ Confirmed: `Dockerfile` exists in project root

### "start.sh not found"
✅ Confirmed: `start.sh` exists in project root

### Build fails with "npm modules not found"
- Check `student-frontend/package.json` exists
- Check `teacher-frontend/package.json` exists
- Verify `npm run build` works locally

### Build fails with "Python dependencies not found"
- Check `backend/requirements.txt` exists
- Verify all packages listed
- Test locally: `pip install -r backend/requirements.txt`

### Migrations fail during build
- Check `backend/manage.py` exists
- Verify `database URL` is set in Railway
- Check for migration conflicts: `python manage.py showmigrations`

### Static files not loading after deployment
- Verify `collectstatic` ran (check logs)
- Check `STATIC_URL` and `STATIC_ROOT` in settings.py
- Verify build copied frontend dist/ files

---

## Local Testing (Docker)

### Build locally
```bash
docker build -t project-sat .
```

### Run locally
```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://... \
  -e SECRET_KEY=... \
  project-sat
```

### Or use Docker Compose
```bash
docker-compose up --build
```

---

## Production Checklist

Before deploying to production:

- [ ] `DEBUG=False` in Railway environment
- [ ] `SECRET_KEY` set to a strong random value
- [ ] `ALLOWED_HOSTS` includes your domain
- [ ] `CORS_ALLOWED_ORIGINS` includes frontend URLs
- [ ] Database migrations run successfully
- [ ] Static files collected
- [ ] Health check endpoint (`/api/docs/`) working
- [ ] Logs show "Listening on 0.0.0.0:8000"

---

## Monitoring After Deployment

### View logs (live)
```powershell
railway logs -f
```

### Check health
```powershell
railway status
```

### Restart service
```powershell
railway restart
```

### Scale replicas
```powershell
railway up --scale backend=2
```

---

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| 502 Bad Gateway | Backend crashed | Check logs: `railway logs` |
| Static files 404 | collectstatic failed | Re-run: `railway run python manage.py collectstatic` |
| Migrations pending | Not run during build | Add `python manage.py migrate` to Dockerfile CMD |
| Database connection error | DATABASE_URL not set | Set in Railway → Project Settings → Variables |
| Build timeout | Takes >30 min | Check node_modules size, optimize dependencies |

---

## Advanced Configuration

### Use multiple replicas
```toml
# railway.toml
[deploy]
replicas = 2  # Auto-scale horizontally
```

### Custom domain
```toml
[deploy]
domain = "yourdomain.com"
```

### Environment-specific
```bash
# Set different env vars per deployment
railway vars set DEBUG=False
railway vars set ENVIRONMENT=production
```

---

## Support

For Railway-specific issues:
- Railway Docs: https://docs.railway.app
- Railway Support: https://railway.app/support
- GitHub Issues: Check your project repo

---

**Status**: ✅ Ready to deploy!
**Last Updated**: Oct 17, 2025

