from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Template)
admin.site.register(models.Field)
