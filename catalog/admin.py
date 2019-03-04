from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from catalog.models import Employee

admin.site.register(Employee, MPTTModelAdmin)