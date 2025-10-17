# Project Setup & Installation Guide

## ✅ Project Status: FULLY OPERATIONAL

All components of the SAT prep platform are now configured and running smoothly.

---

## 🏗️ Architecture Overview

The project consists of three main components:

1. **Backend** (Django REST Framework) - API Server
   - Port: 8000
   - Database: SQLite (local development)
   - Admin: http://localhost:8000/admin

2. **Student Frontend** (React + Vite)
   - Port: 3000
   - URL: http://localhost:3000

3. **Teacher Frontend** (React + Vite)
   - Port: 3001
   - URL: http://localhost:3001

---

## 🚀 Quick Start

### Start All Services

**Terminal 1 - Backend:**
```bash
cd backend
python manage.py runserver
```

**Terminal 2 - Student Frontend:**
```bash
cd student-frontend
npm run dev
```

**Terminal 3 - Teacher Frontend:**
```bash
cd teacher-frontend
npm run dev
```

After starting all services:
- Student Portal: http://localhost:3000
- Teacher Portal: http://localhost:3001
- Backend API: http://localhost:8000
- Django Admin: http://localhost:8000/admin
  - Username: `admin`
  - Password: Set with `python manage.py changepassword admin`

---

## 🔧 Configuration Details

### Backend Configuration (.env)

```properties
SECRET_KEY=django-insecure-8s2k&y^p#x1r*9u_3l%4kz!q0o^a7b3d
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,backend-sato.onrender.com
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001
USE_SQLITE=True
```

**Features:**
- SQLite for local development (easier setup)
- Debug mode enabled for development
- CORS configured for both frontends
- Cross-Origin requests allowed

### Frontend Configuration (.env)

**Student Frontend** (`student-frontend/.env`):
```
VITE_API_BASE_URL=http://localhost:8000
```

**Teacher Frontend** (`teacher-frontend/.env`):
```
VITE_API_BASE_URL=http://localhost:8000
```

---

## 📚 Database

### Current Setup
- **Database Type**: SQLite (file-based)
- **Database Location**: `backend/db.sqlite3`
- **Migrations**: All applied successfully
- **Superuser**: admin (created)

### Running Migrations

```bash
cd backend
python manage.py migrate
```

### Creating a Superuser

```bash
python manage.py createsuperuser
# or
python manage.py createsuperuser --username admin --email admin@example.com
```

---

## 📦 Dependencies

### Backend
All dependencies are listed in `backend/requirements.txt`:
- Django 4.2+
- Django REST Framework
- Django CORS Headers
- djangorestframework-simplejwt (JWT Authentication)
- Pillow (Image handling)
- python-decouple (Environment variables)
- drf-spectacular (API Documentation)

### Student Frontend
Install with: `npm install`
- React 19.1+
- React Router DOM 7.8+
- Axios (HTTP Client)
- Tailwind CSS
- Zustand (State Management)
- Lucide React (Icons)
- React Hot Toast (Notifications)

### Teacher Frontend
Install with: `npm install`
- React 19.1+
- React Router DOM 7.8+
- Axios (HTTP Client)
- Tailwind CSS
- Zustand (State Management)
- Lucide React (Icons)

---

## 🔐 Authentication Flow

1. **Student/Teacher Registration**: POST `/api/auth/register/`
2. **Login**: POST `/api/auth/login/` → Returns `access` and `refresh` tokens
3. **Token Storage**: Tokens stored in localStorage
4. **API Requests**: Include `Authorization: Bearer <token>` header
5. **Token Refresh**: Automatic refresh on 401 errors using `refresh_token`

### Token Locations
- **Access Token**: `localStorage.accessToken` (student) / `localStorage.access_token` (teacher)
- **Refresh Token**: `localStorage.refreshToken` (student) / `localStorage.refresh_token` (teacher)
- **User Data**: `localStorage.userData` (student) / `localStorage.user` (teacher)

---

## 🛠️ API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login
- `POST /api/auth/token/refresh/` - Refresh access token
- `GET/PATCH /api/auth/profile/` - Get/update profile
- `GET/PATCH /api/auth/me/` - Get/update user info

### Student APIs
- `GET /api/student/dashboard/assigned_tests/` - Get assigned tests
- `POST /api/student/test/<id>/start/` - Start a test
- `GET /api/student/test/<id>/section/<section_id>/questions/` - Get section questions
- `POST /api/student/test/<id>/section/<section_id>/answers/` - Submit answers
- `POST /api/student/test/<id>/section/<section_id>/complete/` - Complete section
- `GET /api/student/test/<id>/results/` - Get test results

### Teacher APIs
- `GET /api/teacher/dashboard/` - Dashboard stats
- `GET/POST /api/teacher/tests/` - Manage tests
- `GET/POST /api/teacher/groups/` - Manage student groups
- `GET/POST /api/teacher/assignments/` - Manage test assignments
- `GET /api/teacher/analytics/` - Analytics data
- `GET /api/teacher/library/` - Test library

### API Documentation
- Swagger UI: http://localhost:8000/api/docs/
- OpenAPI Schema: http://localhost:8000/api/schema/

---

## 📱 Key Features

### Student Portal
- View assigned tests
- Take tests with timed sections
- Save answers and review
- View test results
- Access profile settings
- Real-time notifications

### Teacher Portal
- Create and manage tests
- Create student groups
- Assign tests to groups
- View analytics and performance
- Manage questions with images
- Test library for reuse

---

## 🐛 Troubleshooting

### Backend Issues

**Issue**: `ModuleNotFoundError` when running Django
```bash
# Solution: Ensure you're in the backend directory
cd backend
python manage.py runserver
```

**Issue**: Database errors on migration
```bash
# Solution: Check if PostgreSQL is needed, use SQLite for local dev
# Verify USE_SQLITE=True in backend/.env
python manage.py migrate
```

### Frontend Issues

**Issue**: "Cannot GET /", blank page
```bash
# Solution: Ensure Vite dev server is running on correct port
npm run dev
# Verify port in package.json scripts
```

**Issue**: API calls returning 401/403
```bash
# Solution: Check if backend is running
# Verify API_BASE_URL in frontend .env
# Check token expiration in localStorage
```

**Issue**: CORS errors
```bash
# Solution: Verify CORS_ALLOWED_ORIGINS in backend/.env includes frontend URLs
# Ensure both frontend URLs are listed
```

### Port Conflicts

If ports 3000, 3001, or 8000 are already in use:

**Backend**:
```bash
python manage.py runserver 8001
```

**Student Frontend** (update vite.config.js):
```javascript
server: {
  port: 3002,
}
```

**Teacher Frontend** (update vite.config.js):
```javascript
server: {
  port: 3003,
}
```

Then update `.env` files accordingly.

---

## 🚢 Production Deployment

### To Production with Railway PostgreSQL:

1. Update `backend/.env`:
   ```
   DEBUG=False
   DATABASE_URL=postgresql://user:password@host:5432/database
   USE_SQLITE=False
   ```

2. Set allowed hosts:
   ```
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

3. Update frontend `.env` files:
   ```
   VITE_API_BASE_URL=https://api.yourdomain.com
   ```

4. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

5. Deploy using Railway or Render

---

## 📝 Recent Fixes Applied

✅ Fixed migration conflicts (merged 0002_initial and 0002_auto_20251015_1832)
✅ Updated .env files for local development
✅ Corrected teacher-frontend package.json preview script
✅ Configured SQLite for easy local development
✅ Fixed migrations typo (__init.py → __init__.py)
✅ Updated frontend API URLs to localhost:8000
✅ Database migrations completed successfully
✅ Created superuser account for admin access

---

## 📊 Testing

### Backend Tests
```bash
cd backend
python manage.py test
```

### Frontend Linting
```bash
cd student-frontend
npm run lint

cd teacher-frontend
npm run lint
```

### Frontend Build
```bash
cd student-frontend
npm run build

cd teacher-frontend
npm run build
```

---

## 📧 Support & Documentation

- **API Documentation**: http://localhost:8000/api/docs/
- **Database Documentation**: See `backend/DATABASE_SETUP.md`
- **Frontend Notifications**: See `student-frontend/NOTIFICATIONS_PROFILE_SETUP.md`
- **Image Upload API**: See `teacher-frontend/IMAGE_UPLOAD_API.md`

---

## ✨ You're All Set!

Your SAT prep platform is ready to use. Start developing and testing!

**Quick Links:**
- 📱 Student: http://localhost:3000
- 👨‍🏫 Teacher: http://localhost:3001
- 🔌 API: http://localhost:8000
- 📚 Docs: http://localhost:8000/api/docs/
- 🛠️ Admin: http://localhost:8000/admin

Happy coding! 🚀
