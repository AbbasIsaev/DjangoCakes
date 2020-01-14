from django.contrib import admin

from .models import Const


class ConstAdmin(admin.ModelAdmin):
    list_display = ('name', 'params')


admin.site.register(Const, ConstAdmin)
