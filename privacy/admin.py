from django.contrib import admin
from privacy.models import *

class AbstractionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Abstraction,AbstractionAdmin)
class VisibilityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Visibility,VisibilityAdmin)
