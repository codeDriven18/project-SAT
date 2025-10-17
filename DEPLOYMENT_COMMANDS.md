# 🚀 DEPLOYMENT COMMANDS – Copy & Paste

## ⚡ Quick Deploy (3 Commands)

### Command 1: Commit Changes
```powershell
cd c:\proggggg\project-SAT
git add .
git commit -m "Add Railway build configuration: Dockerfile, start.sh, railway.toml"
git push origin main
```

### Command 2: Deploy to Railway
```powershell
railway up
```

### Command 3: Monitor (in new terminal)
```powershell
railway logs -f
```

**Total time to live**: ~3-5 minutes ✅

---

## 📋 Detailed Commands

### Step 1: Initialize Git (if needed)
```powershell
cd c:\proggggg\project-SAT

# Check if git repo exists
git status  # If error, repo doesn't exist

# If needed, create git repo
git init
git remote add origin https://github.com/YOUR_USERNAME/project-SAT.git
git branch -M main
```

### Step 2: Stage and Commit All Changes
```powershell
cd c:\proggggg\project-SAT

# See what changed
git status

# Stage all files
git add .

# Commit with message
git commit -m "Railway build configuration: Add Dockerfile, start.sh, railway.toml, and optimization files"

# Verify commit
git log --oneline -1
```

### Step 3: (Optional) Push to GitHub
```powershell
# If you want to push to GitHub
git push origin main

# If push fails, link remote first
git remote set-url origin https://github.com/YOUR_USERNAME/project-SAT.git
git push -u origin main
```

### Step 4: Deploy to Railway
```powershell
# Make sure you've done: railway login && railway link -p b64abf5f-0974-4a4e-a9a5-329b921e000f

# Deploy
railway up

# Watch build progress
# Expected: "✓ Deployment successful"
```

### Step 5: Monitor Deployment
```powershell
# Terminal 1: Watch logs live
railway logs -f

# Terminal 2: Check status
railway status

# Terminal 3: View in browser
railway open
```

---

## 🔧 Post-Deployment Commands

### View Environment Variables
```powershell
railway vars
```

### Create Superuser
```powershell
railway run python manage.py createsuperuser
```

### View Logs (last 50 lines)
```powershell
railway logs --tail 50
```

### Run Migrations (if needed)
```powershell
railway run python manage.py migrate
```

### Reset Database (⚠️ careful!)
```powershell
railway run python manage.py flush --no-input
```

### Collect Static Files (if needed)
```powershell
railway run python manage.py collectstatic --noinput
```

### Restart Service
```powershell
railway restart
```

### Scale Replicas (2x servers)
```powershell
railway up --scale backend=2
```

---

## 🧪 Local Testing (Before Deploy)

### Test Dockerfile Locally
```bash
# Build image
docker build -t project-sat .

# Run container
docker run -p 8000:8000 \
  -e DEBUG=True \
  -e DATABASE_URL=postgresql://user:pass@host/dbname \
  -e SECRET_KEY=test-secret-key \
  project-sat
```

### Test with Docker Compose
```bash
docker-compose up --build
```

---

## 🔍 Debugging Commands

### Check Logs for Errors
```powershell
railway logs | grep -i error
railway logs | grep -i fail
railway logs | grep -i exception
```

### Test Health Endpoint
```powershell
# Get your Railway URL
railway open  # Opens in browser

# Test API (replace URL)
curl https://your-app.railway.app/api/docs/
curl https://your-app.railway.app/api/schema/
```

### SSH Into Container (if available)
```powershell
railway run bash

# Inside container:
python manage.py shell  # Django shell
python manage.py showmigrations  # List migrations
python manage.py dbshell  # Connect to database
```

---

## 📊 Monitoring Commands

### Real-time Logs
```powershell
railway logs -f
```

### Last 100 lines
```powershell
railway logs --tail 100
```

### Logs from specific time
```powershell
railway logs --since "30 minutes ago"
```

### Filter logs by keyword
```powershell
railway logs | findstr "ERROR"
railway logs | findstr "migration"
railway logs | findstr "gunicorn"
```

---

## ⚙️ Configuration Commands

### Set Environment Variable
```powershell
railway var set DEBUG=False
railway var set SECRET_KEY=your-strong-secret-key
railway var set ALLOWED_HOSTS=your-domain.railway.app
```

### View Specific Variable
```powershell
railway var get DEBUG
railway var get DATABASE_URL
```

### Remove Variable
```powershell
railway var remove DEBUG
```

### Export All Variables
```powershell
railway vars > env-vars.txt
```

---

## 🚨 Rollback Commands

### List Deployments
```powershell
railway deployments list
```

### Rollback to Previous
```powershell
railway deployments rollback <deployment-id>
```

### Or via Dashboard
```
Settings → Deployments → Select Previous → Redeploy
```

---

## 🧹 Cleanup Commands

### Remove Local Build
```powershell
docker rmi project-sat
```

### Prune Docker (remove unused)
```powershell
docker system prune -a
```

### Clean Railway Cache
```powershell
railway build --no-cache
```

---

## 📞 Support Commands

### Check Railway CLI Version
```powershell
railway --version
```

### Check Railway Status
```powershell
railway status
```

### Open Railway Dashboard
```powershell
railway open
```

### Get Help
```powershell
railway --help
railway up --help
railway logs --help
```

---

## 🎯 Complete Deployment Flow

```powershell
# 1. Navigate to project
cd c:\proggggg\project-SAT

# 2. Verify git is set up
git status

# 3. Stage and commit changes
git add .
git commit -m "Add Railway build configuration"

# 4. Push to remote (optional)
git push origin main

# 5. Deploy to Railway
railway up

# 6. Monitor logs (new terminal)
railway logs -f

# 7. When deployment complete:
railway open  # Opens in browser

# 8. Verify deployment
# - Visit https://app.railway.app/api/docs/
# - Check status: railway status
# - View logs: railway logs --tail 20
```

---

## ⏱️ Expected Timeline

```
0:00 - Start: railway up
0:30 - Building base images
1:00 - Installing dependencies
1:30 - Building frontends
2:00 - Running migrations
2:30 - Collecting static files
3:00 - Starting gunicorn
3:30 - ✅ Deployment successful!
```

---

## 🆘 Troubleshooting Quick Ref

### Build fails
```powershell
railway logs -f  # Watch in real-time
railway logs --tail 50  # Last 50 lines
```

### 502 Bad Gateway
```powershell
railway status  # Check if running
railway restart  # Restart service
railway logs -f  # Check errors
```

### Database error
```powershell
railway vars | findstr DATABASE_URL
railway run python manage.py migrate  # Try migrate again
```

### Static files 404
```powershell
railway logs | findstr collectstatic
railway run python manage.py collectstatic --noinput
```

---

## 🎉 Success Indicators

When deployment succeeds, you should see:

```
[Railway] Build completed successfully
[Railway] Starting service...
[Railway] Listening on 0.0.0.0:8000
[Railway] ✓ Deployment successful
```

Then:
- ✅ `railway status` shows "deployed"
- ✅ `https://app.railway.app/api/docs/` loads
- ✅ `https://app.railway.app/admin/` loads
- ✅ No errors in `railway logs`

---

## 💾 Reference

### Documentation Files
- `DEPLOY_NOW.md` ← You are here
- `RAILWAY_BUILD_CONFIG.md` ← Build details
- `RAILWAY_READY_TO_DEPLOY.md` ← Deployment status
- `COMPLETE_SUMMARY.md` ← Full overview

### Config Files
- `Dockerfile` ← Build instructions
- `railway.toml` ← Deployment settings
- `start.sh` ← Fallback start script
- `.dockerignore` ← Build optimization
- `.railwayignore` ← Deploy optimization

---

**Status**: ✅ READY TO DEPLOY
**Next**: Run `railway up` 🚀

