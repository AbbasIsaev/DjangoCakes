import uuid

from django.contrib.auth.models import User
from django.db import models

from photo.models import Photo


class Cake(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, verbose_name='Наименование')
    text = models.TextField(verbose_name='Описание')
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name='Цена')
    photos = models.ManyToManyField(Photo, default=None, blank=True, verbose_name='Фото')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    created_by = models.ForeignKey(User, blank=True, null=True, default=None,
                                   on_delete=models.SET_NULL,
                                   related_name="created_cake", verbose_name='Создал')
    updated_by = models.ForeignKey(User, blank=True, null=True, default=None,
                                   on_delete=models.SET_NULL,
                                   related_name="updated_cake", verbose_name='Обновил')

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты (Cakes)'
        ordering = ['-updated']
