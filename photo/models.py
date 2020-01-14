import uuid

from PIL import Image
from django.db import models


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.url.url

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Photo, self).save()

        image = Image.open(self.url.path)

        w_size = 1280
        h_size = 1280
        if image.height > h_size or image.width > w_size:
            resize = (w_size, h_size)
            image.thumbnail(resize)
            image.save(self.url.path)
