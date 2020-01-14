from django.contrib import admin

from .models import Cake


class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'price',
                    'created', 'created_by', 'updated', 'updated_by')
    readonly_fields = ['created', 'created_by', 'updated', 'updated_by']


admin.site.register(Cake, CakeAdmin)
