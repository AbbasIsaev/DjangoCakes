from django.contrib import admin

from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('url',)


admin.site.register(Photo, PhotoAdmin)
