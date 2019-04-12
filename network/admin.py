from django.contrib import admin

from django.contrib.auth.models import User


from network.models import *
# Register your models here.




class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City,CityAdmin)



class ContactTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactType,ContactTypeAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact,ContactAdmin)







