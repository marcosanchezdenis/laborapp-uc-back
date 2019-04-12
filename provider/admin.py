from django.contrib import admin

from provider.models import *

class ProblemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Problem,ProblemAdmin)

class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service,ServiceAdmin)

class CommentTabularInline(admin.TabularInline):
    model = Comment


class ProviderDataTabularInline(admin.TabularInline):
    model = ProviderData

class ProviderAdmin(admin.ModelAdmin):
    inlines = [ProviderDataTabularInline,CommentTabularInline]
admin.site.register(Provider,ProviderAdmin)

class ProviderDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProviderData,ProviderDataAdmin)