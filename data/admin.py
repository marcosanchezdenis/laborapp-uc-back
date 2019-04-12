from django.contrib import admin


from data.models import * 


# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Property,PropertyAdmin)
class PropertyTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(PropertyType,PropertyTypeAdmin)