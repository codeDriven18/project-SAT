# Pre-Deployment & Verification Checklist

## ✅ Configuration Verification

Run these commands to verify setup:

```powershell
# Verify Python & Django
cd backend
python --version  # Should be 3.13+
python manage.py check  # Should show "System check identified no issues"

# Verify PostgreSQL configuration
python manage.py dbshell --help  # Should show options (doesn't need to connect)

# List all migrations (should show no conflicts)
python manage.py showmigrations

# Verify static files location
python manage.py collectstatic --dry-run --no-input | Select-Object -First 5

# Verify .env is loaded
python -c "from decouple import config; print(f'DEBUG={config(\"DEBUG\")}'); print(f'DB host visible in URL: postgresql://...')"
```

---

## ✅ Frontend Verification

```powershell
# Student Frontend
cd student-frontend
npm list react react-dom  # Should show v19+
npm run build 2>&1 | Select-Object -Last 10  # Should build successfully

# Teacher Frontend
cd teacher-frontend
npm list react react-dom  # Should show v19+
npm run build 2>&1 | Select-Object -Last 10  # Should build successfully
```

---

## ✅ API Health Check (After Backend Starts)

```powershell
# Start backend in one terminal:
cd backend
python manage.py runserver

# In another terminal, test endpoints:
curl http://localhost:8000/api/docs/  # Should return Swagger UI
curl http://localhost:8000/api/schema/  # Should return OpenAPI schema

# Test auth endpoint (without auth, should be 401)
curl -X GET http://localhost:8000/api/auth/me/  # Should get 401 Unauthorized

# Test student endpoint (without auth, should be 401)
curl -X GET http://localhost:8000/api/student/dashboard/assigned_tests/  # Should get 401 Unauthorized
```

---

## ✅ Database Health (After Migrations)

```powershell
# Connect to Django shell
railway run python manage.py shell

# Inside shell:
from django.contrib.auth import get_user_model
User = get_user_model()
print(f"Total users: {User.objects.count()}")  # Should be >= 1 (at least superuser)

from apps.tests.models import Test, Section, Question
print(f"Tests: {Test.objects.count()}")
print(f"Sections: {Section.objects.count()}")
print(f"Questions: {Question.objects.count()}")

exit()
```

---

## ✅ Before `railway up` Deployment

- [ ] Backend `.env` has `DATABASE_URL` (from Railway)
- [ ] Backend `.env` has `DEBUG=False` (for production)
- [ ] Backend `.env` has correct `SECRET_KEY` (strong, not default)
- [ ] Migrations have been run: `railway run python manage.py migrate`
- [ ] Superuser has been created: `railway run python manage.py createsuperuser`
- [ ] Static files collected: `railway run python manage.py collectstatic --noinput`
- [ ] `railway.toml` exists and has correct `startCommand`
- [ ] `Procfile` exists and has backend start command
- [ ] `requirements.txt` is up-to-date: `pip freeze > requirements.txt` (if needed)
- [ ] Frontend builds succeed: `npm run build` (in each frontend folder)
- [ ] Frontend `.env` files point to correct backend URL:
  - Dev: `VITE_API_BASE_URL=http://localhost:8000`
  - Prod: `VITE_API_BASE_URL=https://<railway-backend-url>`
- [ ] `python manage.py check` passes with no warnings
- [ ] Git is clean: `git status` (optional, but recommended before deploy)

---

## ✅ Production Environment Setup (Railway Dashboard)

Ensure these are set in Railway project settings:

- ✅ `DEBUG=False` (security)
- ✅ `SECRET_KEY=<strong-random-key>` (not default)
- ✅ `ALLOWED_HOSTS=<your-railway-domain>`
- ✅ `CORS_ALLOWED_ORIGINS=<frontend-urls>`
- ✅ `DATABASE_URL` (auto-set by Railway PostgreSQL plugin)

---

## ✅ Post-Deployment Verification

After `railway up` succeeds:

```powershell
# View deployment
railway open

# Check logs for errors
railway logs --tail 50

# Verify health check passes
railway status

# Test live endpoints
curl https://<your-railway-domain>/api/docs/
curl https://<your-railway-domain>/api/schema/

# Test live admin
https://<your-railway-domain>/admin/
# Login with superuser credentials
```

---

## ✅ Rollback Plan

If deployment fails:

```powershell
# Check logs
railway logs --tail 100

# Redeploy previous version
railway up --force

# Or rollback via Railway dashboard
# Settings → Deployments → select previous version → Redeploy
```

---

## ✅ Monitoring & Maintenance

After deployed:

- Monitor logs: `railway logs -f` (live stream)
- Check database: `railway run python manage.py dbshell`
- Clear cache: `railway run python manage.py clearcache` (if using cache)
- Run management tasks: `railway run python manage.py <command>`

---

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| 502 Bad Gateway | Check backend logs: `railway logs` |
| Static files not loading | Ensure `collectstatic` was run |
| Database connection error | Verify `DATABASE_URL` is set in Railway env |
| CORS errors | Check `CORS_ALLOWED_ORIGINS` in backend `.env` |
| "Secret key not set" | Set `SECRET_KEY` in Railway environment |
| Migrations failed | Run `railway run python manage.py migrate` again |
| 404 on admin | Ensure migrations ran (includes auth tables) |

---

## 📋 Deployment Checklist Summary

- [ ] `railway login` & `railway link` completed
- [ ] Migrations run: `railway run python manage.py migrate`
- [ ] Superuser created: `railway run python manage.py createsuperuser`
- [ ] Static files collected: `railway run python manage.py collectstatic --noinput`
- [ ] All verification checks pass
- [ ] Production `.env` settings verified in Railway dashboard
- [ ] Ready to deploy: `railway up`

---

**Once complete, you're ready for production! 🚀**

