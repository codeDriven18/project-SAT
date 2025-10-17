# Project Setup & Deployment Guide

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.13+
- Node.js 18+
- PostgreSQL (remote Railway DB – no local install needed)
- Railway CLI (will install if not present)

### Step 1: Install Railway CLI & Link Project
```powershell
# Install Railway CLI globally
npm install -g railway

# Authenticate to Railway (opens browser)
railway login

# Link to the project
railway link -p b64abf5f-0974-4a4e-a9a5-329b921e000f

# Verify connection
railway variables
```

### Step 2: Initialize Database (Run Migrations)
```powershell
cd backend

# Run migrations on Railway (migrations run in Railway environment where DB is accessible)
railway run python manage.py migrate

# Create Django superuser
railway run python manage.py createsuperuser

# Collect static files
railway run python manage.py collectstatic --noinput
```

### Step 3: Start Development Servers

**Terminal 1: Backend**
```powershell
cd backend
python manage.py runserver
# → Django at http://localhost:8000/admin
```

**Terminal 2: Student Frontend**
```powershell
cd student-frontend
npm run dev
# → http://localhost:3000
```

**Terminal 3: Teacher Frontend**
```powershell
cd teacher-frontend
npm run dev
# → http://localhost:3001
```

---

## 📋 File Structure & Configuration

```
project-SAT/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env                          # ← Railway DATABASE_URL here
│   ├── eduplatform/
│   │   ├── settings.py               # ← PostgreSQL config
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── apps/
│       ├── tests/
│       ├── users/
│       ├── analytics/
│       └── notifications/
│
├── student-frontend/
│   ├── package.json
│   ├── .env                          # ← VITE_API_BASE_URL=http://localhost:8000
│   ├── vite.config.js
│   └── src/
│
├── teacher-frontend/
│   ├── package.json
│   ├── .env                          # ← VITE_API_BASE_URL=http://localhost:8000
│   ├── vite.config.js
│   └── src/
│
├── railway.toml                       # ← Railway deployment config
├── Procfile                           # ← Process file for Railway
└── README.md
```

---

## ✅ Configuration Checklist

- [x] `backend/.env` – DATABASE_URL set to Railway Postgres
- [x] `backend/eduplatform/settings.py` – PostgreSQL only (no SQLite)
- [x] `student-frontend/.env` – VITE_API_BASE_URL=http://localhost:8000
- [x] `teacher-frontend/.env` – VITE_API_BASE_URL=http://localhost:8000
- [x] `railway.toml` – Deployment config with gunicorn
- [x] `Procfile` – Backend startup command
- [x] `requirements.txt` – All dependencies listed
- [x] `package.json` (both frontends) – Dependencies listed
- [x] Django migrations conflict resolved
- [x] Railway CLI installed and linked
- [ ] Migrations run successfully (pending your `railway link`)
- [ ] Superuser created (pending migrations)
- [ ] Static files collected (pending migrations)
- [ ] Deployment tested locally
- [ ] Deployed to Railway (`railway up`)

---

## 🛠️ Common Commands

### Django Management
```powershell
# Run migrations
railway run python manage.py migrate

# Create superuser
railway run python manage.py createsuperuser

# Collect static files
railway run python manage.py collectstatic --noinput

# Make migrations
python manage.py makemigrations

# Check system
python manage.py check

# Shell
railway run python manage.py shell
```

### Frontend Development
```powershell
# Install dependencies
npm install

# Run dev server
npm run dev

# Build for production
npm run build

# Lint
npm run lint
```

### Railway
```powershell
# View variables
railway variables

# Run command in Railway environment
railway run <command>

# Deploy
railway up

# View logs
railway logs

# Status
railway status
```

---

## 🌐 API Endpoints

### Authentication
- `POST /api/auth/register/` – Register user
- `POST /api/auth/login/` – Login (returns access & refresh tokens)
- `POST /api/auth/token/refresh/` – Refresh access token
- `GET /api/auth/me/` – Get current user profile
- `PATCH /api/auth/me/` – Update profile

### Student
- `GET /api/student/dashboard/assigned_tests/` – Assigned tests
- `POST /api/student/test/<id>/start/` – Start test
- `GET /api/student/test/<id>/section/<sec_id>/questions/` – Get questions
- `POST /api/student/test/<id>/section/<sec_id>/answers/` – Submit answers
- `POST /api/student/test/<id>/complete/` – Complete test
- `GET /api/student/test/<id>/results/` – Get results

### Teacher
- `GET /api/teacher/dashboard/` – Dashboard stats
- `GET /api/teacher/tests/` – List tests
- `POST /api/teacher/tests/` – Create test
- `GET /api/teacher/groups/` – List groups
- `POST /api/teacher/groups/` – Create group
- `GET /api/teacher/analytics/test_analytics/` – Test analytics
- `GET /api/teacher/library/` – Test library

### Documentation
- `GET /api/docs/` – Swagger UI (auto-generated)
- `GET /api/schema/` – OpenAPI schema

---

## 🚀 Deployment to Railway

### Prerequisites
- `railway login` completed
- `railway link` completed
- Migrations run successfully

### Deploy
```powershell
cd c:\proggggg\project-SAT
railway up
```

### What Happens
1. Railway builds the project (installs dependencies, runs collectstatic)
2. Railway runs the Procfile (starts gunicorn on port specified by Railway)
3. Railway connects to the PostgreSQL database (DATABASE_URL set automatically)
4. App is live at `https://<railway-domain>.railway.app`

### Post-Deployment
1. Verify at Railway dashboard
2. Run admin panel: `https://<railway-domain>.railway.app/admin/`
3. Check logs: `railway logs`
4. Scale if needed: `railway up --scale backend=2` (multiple replicas)

---

## 🔧 Troubleshooting

### "Cannot reach database" locally
- **Expected behavior**: Railway's internal DB host is only accessible from Railway's network
- **Solution**: Use `railway run` to execute Django commands (runs inside Railway where DB is accessible)
- **Local dev**: Migrations run once via `railway run`; then `python manage.py runserver` connects to Railway's public proxy (if accessible) or use local SQLite fallback (not recommended for production)

### Migrations conflict
- **Error**: "Conflicting migrations detected"
- **Solution**: Already resolved in this setup; run `python manage.py migrate` to confirm

### Static files not loading
- **Dev**: `python manage.py runserver` auto-serves static files
- **Prod**: Ensure `railway run python manage.py collectstatic --noinput` was run

### Frontend can't reach backend
- **Check**: `student-frontend/.env` and `teacher-frontend/.env` have correct `VITE_API_BASE_URL`
- **Dev**: Should be `http://localhost:8000`
- **Prod**: Should be your Railway backend URL (e.g., `https://backend.railway.app`)

### Port already in use
```powershell
# Find process using port
netstat -ano | findstr :8000

# Kill process (replace PID with process ID)
taskkill /PID <PID> /F

# Or use different port
python manage.py runserver 8001
```

---

## 📝 Notes

- Database: Railway PostgreSQL (13+ compatible)
- ORM: Django ORM with psycopg2 driver
- API Framework: Django REST Framework with drf-spectacular
- Frontend: React 19 with Vite, Tailwind CSS
- Auth: JWT (djangorestframework-simplejwt)
- Deployment: Railway (auto-scaling, PostgreSQL managed)

---

## 🆘 Support

For issues:
1. Check `railway logs` for backend errors
2. Check browser console for frontend errors
3. Verify `.env` files have correct values
4. Confirm migrations have run: `railway run python manage.py showmigrations`
5. Test API manually: `railway run python manage.py shell` → run test queries

---

**Last Updated**: Oct 17, 2025

