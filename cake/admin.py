from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from photo.admin import wrapper_photo
from server.utils.handler import ExceptionHandler
from .models import Cake


class CakeAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание')

    class Meta:
        model = Cake
        fields = '__all__'


class CakeAdmin(admin.ModelAdmin):
    form = CakeAdminForm
    list_display = ('name', 'text', 'price',
                    'created', 'created_by', 'updated', 'updated_by', 'sample_photos')
    list_display_links = ('name', 'text')
    list_editable = ('price',)
    readonly_fields = ['sample_photos', 'created', 'created_by', 'updated', 'updated_by']
    search_fields = ('name', 'text')
    save_on_top = True

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

    sample_photos.short_description = "Фото"


admin.site.register(Cake, CakeAdmin)
