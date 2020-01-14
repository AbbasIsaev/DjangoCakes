import uuid

from django.contrib.auth.models import User
from django.db import models

from photo.models import Photo


class Cake(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    text = models.TextField()
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    photos = models.ManyToManyField(Photo, default=None, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, blank=True, null=True, default=None,
                                   on_delete=models.SET_NULL,
                                   related_name="created_cake")
    updated_by = models.ForeignKey(User, blank=True, null=True, default=None,
                                   on_delete=models.SET_NULL,
                                   related_name="updated_cake")
