# my_script.py

import os
import django
from django.conf import settings

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskTracker.settings')
django.setup()

# Import your models
from tt.models import Team

def main():
    teams = Team.objects.all()
    for team in teams:
        print(f"Team ID: {team.id}, Name: {team.name}")

if __name__ == "__main__":
    main()
