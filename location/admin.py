from django.contrib import admin

from location.models import *
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location,LocationAdmin)