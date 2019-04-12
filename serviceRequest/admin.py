from django.contrib import admin

from serviceRequest.models import *

class MessageTabularInline(admin.TabularInline):
    model = Message

class RequestStateAdmin(admin.ModelAdmin):
    pass
admin.site.register(RequestState,RequestStateAdmin)

class RequestAdmin(admin.ModelAdmin):
    inlines =  [ MessageTabularInline]
admin.site.register(Request,RequestAdmin)