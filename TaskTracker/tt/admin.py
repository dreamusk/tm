# myapp/admin.py

from django.contrib import admin
from .models import Team, Employee, Work, Project, Manage

admin.site.register(Team)
admin.site.register(Employee)
admin.site.register(Work)
admin.site.register(Project)
admin.site.register(Manage)
