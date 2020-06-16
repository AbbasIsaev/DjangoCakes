from django.contrib import admin
from django.utils.safestring import mark_safe

from server.utils.handler import ExceptionHandler
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'sample_photo')
    readonly_fields = ['sample_photo']

    def sample_photo(self, obj):
        """Показываем картинку. https://books.agiliq.com/projects/django-admin-cookbook/en/latest/imagefield.html"""
        if obj.url.name == '':
            return '-'
        try:
            width = obj.url.width
            height = obj.url.height
            url = obj.url.url
        except Exception as err:
            err_h = ExceptionHandler(err)
            return mark_safe('%s <strong>Ошибка: %s</strong>' % (obj.url.name, err_h))

        html = wrapper_photo(80, 80, width, height, url)
        return mark_safe(html)

    sample_photo.short_description = "Фото"


admin.site.register(Photo, PhotoAdmin)


def wrapper_photo(w_size, h_size, width, height, url):
    if width > height:
        k = width / w_size
    else:
        k = height / h_size
    width = width / k
    height = height / k
    html = '<a href="{url}" target="_blank">' \
           '    <img src="{url}" alt="{url}" width="{width}" height={height} />' \
           '</a>'.format(url=url,
                         width=width,
                         height=height)
    return html
