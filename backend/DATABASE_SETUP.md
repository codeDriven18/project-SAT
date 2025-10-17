# Database Setup for Render Deployment

## Configuration

Your Django application is now configured to use Render's PostgreSQL database. Here's what you need to do:

### 1. Set Environment Variables in Render

In your Render dashboard, add these environment variables:

```
DATABASE_URL=postgresql://username:password@hostname:port/database_name
SECRET_KEY=your-secret-key-here
DEBUG=False
```

### 2. Database URL Format

The `DATABASE_URL` should look like this:
```
postgresql://username:password@dpg-xxxxx-a.oregon-postgres.render.com:5432/database_name
```

### 3. Current Configuration

The settings.py file is now configured to:
- Use `DATABASE_URL` if provided (for Render deployment)
- Fall back to individual database settings if `DATABASE_URL` is not set
- Enable SSL connections for production
- Set appropriate security headers for production

### 4. Running Migrations

Once you deploy to Render with the `DATABASE_URL` set, the migrations will run automatically during the build process.

### 5. Local Development

For local development, you can either:
- Set up a local PostgreSQL database
- Use the individual database settings in your local `.env` file
- Set `DEBUG=True` to use SQLite (though this is not recommended for production)

## Security Notes

- Never commit your actual `DATABASE_URL` or `SECRET_KEY` to version control
- Use Render's environment variable system to securely store these values
- The application is configured with SSL requirements for production
