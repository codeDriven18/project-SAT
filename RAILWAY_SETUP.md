# Railway PostgreSQL Setup for Local Development

## Status
✅ Railway CLI installed (v2.0.17)
✅ Backend config updated to use Railway DATABASE_URL
✅ Django system checks passed

## Next Steps (You Do These)

### 1. Login to Railway
```powershell
railway login
```
This will open a browser for authentication. Complete the login in your Railway account.

### 2. Link to the Project
From the `c:\proggggg\project-SAT` directory (project root):
```powershell
railway link -p b64abf5f-0974-4a4e-a9a5-329b921e000f
```

If successful, you'll see confirmation. If it says "Project not found", verify you logged in to the correct Railway account.

### 3. Verify Project Link
```powershell
railway variables
```
You should see the PostgreSQL environment variables (DATABASE_URL, DATABASE_PUBLIC_URL, PGUSER, PGPASSWORD, etc.)

---

## After Linking: Run Migrations and Start Backend

Once you've completed steps 1–3 above, run these commands from the backend folder:

### Run Migrations on Railway
```powershell
cd c:\proggggg\project-SAT\backend
railway run python manage.py migrate
```

### Create Superuser (Interactive)
```powershell
railway run python manage.py createsuperuser
```
Follow the prompts to create a Django admin account.

### Collect Static Files (for deployment)
```powershell
railway run python manage.py collectstatic --noinput
```

---

## Development: Run Backend Locally (Against Railway DB)

Once migrations are done, start the dev server locally:

```powershell
cd c:\proggggg\project-SAT\backend

# Activate venv (if using one)
.\.venv\Scripts\Activate  # or your venv path

# Start Django dev server (will use DATABASE_URL from .env to connect to Railway)
python manage.py runserver
```

Should show:
```
Starting development server at http://127.0.0.1:8000/
```

---

## Start Frontends

In separate terminals:

### Student Frontend
```powershell
cd c:\proggggg\project-SAT\student-frontend
npm install  # if not already done
npm run dev
```
→ http://localhost:3000

### Teacher Frontend
```powershell
cd c:\proggggg\project-SAT\teacher-frontend
npm install  # if not already done
npm run dev
```
→ http://localhost:3001

---

## Deployment to Railway

When ready to deploy:

```powershell
# Ensure you're in the project root
cd c:\proggggg\project-SAT

# Deploy to Railway
railway up
```

Railway will:
- Build the backend (collect static, run migrations automatically if configured)
- Deploy to the Railway domain
- Use the Railway PostgreSQL database

---

## Troubleshooting

### "railway: command not found"
- Make sure npm global packages are in your PATH
- Or reinstall: `npm install -g railway`

### "Project not found" during link
- Verify you ran `railway login` and authenticated to the correct account
- Check project ID: `b64abf5f-0974-4a4e-a9a5-329b921e000f`

### "Cannot reach database" locally
- This is expected; the proxy host `switchyard.proxy.rlyw.net` is blocked
- Use `railway run` commands to execute Django commands (they run in Railway's environment where the DB is accessible)
- For local dev, migrate once and then work against the remote DB (or use a local SQLite if you prefer dev-only work)

### Static files not served locally
- For local dev with `python manage.py runserver`, Django auto-serves static files
- For production, ensure `collectstatic` is run: `railway run python manage.py collectstatic --noinput`

---

## Files Updated

- ✅ `backend/.env` – Set DATABASE_URL to Railway public proxy
- ✅ `backend/eduplatform/settings.py` – Use DATABASE_URL exclusively (no SQLite fallback)
- ✅ `student-frontend/.env` – VITE_API_BASE_URL = http://localhost:8000 (or your backend URL)
- ✅ `teacher-frontend/.env` – VITE_API_BASE_URL = http://localhost:8000 (or your backend URL)
- ✅ Removed typo migration file: `apps/tests/migrations/__init.py`

---

## Quick Checklist for Deployment

- [ ] Run `railway login`
- [ ] Run `railway link -p b64abf5f-0974-4a4e-a9a5-329b921e000f`
- [ ] Run `railway run python manage.py migrate`
- [ ] Run `railway run python manage.py createsuperuser`
- [ ] Run `railway run python manage.py collectstatic --noinput`
- [ ] Test locally: `python manage.py runserver` (should connect to Railway DB)
- [ ] Deploy: `railway up`
- [ ] Verify deployment URL in Railway dashboard

