from django.contrib import admin
from .models import Employee, Position

admin.site.register(Employee, Position)