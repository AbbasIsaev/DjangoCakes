from datetime import datetime

from django.utils.deconstruct import deconstructible
from django_webdav_storage.storage import WebDavStorage
from storages.backends.sftpstorage import SFTPStorage

from server.settings import STORAGE_DIR


class SFTPFileSystemStorage(SFTPStorage):
    """
    name - имя картинки. Изменить если нужно переименовать название картинки перед сохранением
    """

    def _save(self, name, content):
        return super(SFTPFileSystemStorage, self)._save(name, content)


@deconstructible
class WebDavFileSystemStorage(WebDavStorage):
    """
    name - имя картинки. Изменить если нужно переименовать название картинки перед сохранением
    """

    def _save(self, name, content):
        name = '{STORAGE_DIR}_{date}_{name}'.format(
            STORAGE_DIR=STORAGE_DIR,
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            name=name)
        return super(WebDavFileSystemStorage, self)._save(name, content)
