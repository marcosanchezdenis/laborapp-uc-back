from django.contrib import admin


from customer.models import *


class CustomerDataTabularInline(admin.TabularInline):
    model = CustomerData

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerDataTabularInline]
admin.site.register(Customer,CustomerAdmin)



class CustomerDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomerData,CustomerDataAdmin)