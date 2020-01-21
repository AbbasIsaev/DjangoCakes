import uuid

from django.db import models

from server.storage import SFTPFileSystemStorage

SFS = SFTPFileSystemStorage()


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO не создается директория upload_to='photos', вместо этого меняется имя файла на 'photos\имя_файла'
    url = models.ImageField(upload_to='', storage=SFS)

    def __str__(self):
        return self.url.url


# TODO Уменьшить размер картинки
"""
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
"""
