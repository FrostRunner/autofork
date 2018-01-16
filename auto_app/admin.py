from django.contrib import admin

from .models import AutoModel


class AutoModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'model')


admin.site.register(AutoModel, AutoModelAdmin)
