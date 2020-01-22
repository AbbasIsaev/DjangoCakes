from django.contrib import admin
from django.utils.safestring import mark_safe

from photo.admin import wrapper_photo
from server.utils.handler import ExceptionHandler
from .models import Cake


class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'price',
                    'created', 'created_by', 'updated', 'updated_by')
    readonly_fields = ['sample_photos', 'created', 'created_by', 'updated', 'updated_by']

    def sample_photos(self, obj_cake):
        """Показываем картинку. https://books.agiliq.com/projects/django-admin-cookbook/en/latest/imagefield.html"""
        photos_all = obj_cake.photos.all()
        html = ''
        for obj in photos_all:
            try:
                width = obj.url.width
                height = obj.url.height
                url = obj.url.url
            except Exception as err:
                err_h = ExceptionHandler(err)
                html += '<p>%s <strong>Ошибка: %s</strong></p>' % (obj.url.name, err_h)
                continue

            html += wrapper_photo(80, 80, width, height, url)
        return mark_safe(html)


admin.site.register(Cake, CakeAdmin)
