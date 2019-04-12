from django.contrib import admin

# Register your models here.


class SearchAdmin(admin.ModelAdmin):
    pass
admin.site.register(Search,SearchAdmin)