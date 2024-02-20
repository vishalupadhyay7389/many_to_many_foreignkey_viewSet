from django.contrib import admin
from .models import Student , School , Activity

# Register your models here.
admin.site.register([Student,School,Activity])
