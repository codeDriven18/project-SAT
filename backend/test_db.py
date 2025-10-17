#!/usr/bin/env python
"""
Simple script to test database connection
Run this after setting up your DATABASE_URL environment variable
"""

import os
import sys
import django
from pathlib import Path

# Add the backend directory to Python path
sys.path.append(str(Path(__file__).parent))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduplatform.settings')
django.setup()

from django.db import connection
from django.core.management import execute_from_command_line

def test_database_connection():
    """Test the database connection"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("✅ Database connection successful!")
            print(f"Query result: {result}")
            return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def run_migrations():
    """Run database migrations"""
    try:
        print("🔄 Running migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        print("✅ Migrations completed successfully!")
        return True
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing database configuration...")
    
    # Check if DATABASE_URL is set
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        print(f"📡 DATABASE_URL is set: {database_url[:50]}...")
    else:
        print("⚠️  DATABASE_URL not set, using fallback configuration")
    
    # Test connection
    if test_database_connection():
        # Run migrations if connection is successful
        run_migrations()
    else:
        print("\n💡 Make sure to set your DATABASE_URL environment variable")
        print("   Example: export DATABASE_URL='postgresql://user:pass@host:port/db'")
