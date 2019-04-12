from django.contrib import admin

from score.models import *


class ScoreSystemValueTabularInline(admin.TabularInline):
    model = ScoreSystemValue


class SkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(Skill,SkillAdmin)


class ScoreSystemAdmin(admin.ModelAdmin):
    inlines = [ScoreSystemValueTabularInline]
admin.site.register(ScoreSystem,ScoreSystemAdmin)



class ScoreSystemValueAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScoreSystemValue,ScoreSystemValueAdmin)


class ScoreProviderAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScoreProvider,ScoreProviderAdmin)


class ScoreCustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScoreCustomer,ScoreCustomerAdmin)