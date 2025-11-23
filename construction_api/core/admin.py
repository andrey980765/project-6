# core/admin.py
from django.contrib import admin
from .models import Client, Project, Building, Contractor

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Building)
admin.site.register(Contractor)


# Register your models here.
