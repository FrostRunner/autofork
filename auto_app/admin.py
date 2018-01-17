from django.contrib import admin

from .models import AutoModel, AutoMake


class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'model')

class AutoMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


admin.site.register(AutoModel, AutoModelAdmin)
admin.site.register(AutoMake, AutoMakeAdmin)
