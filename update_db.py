import os
import django
from django.db import connection

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LearnEase_Portal.settings")
django.setup()

# Alter the table
with connection.cursor() as cursor:
    cursor.execute("ALTER TABLE dashboard_schedule ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP;")
    cursor.execute("ALTER TABLE dashboard_schedule ADD COLUMN updated_at DATETIME DEFAULT CURRENT_TIMESTAMP;")
print("Columns added successfully!")
