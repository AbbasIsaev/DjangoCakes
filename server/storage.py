from storages.backends.sftpstorage import SFTPStorage


class SFTPFileSystemStorage(SFTPStorage):
    """
    name - имя картинки. Изменить если нужно переименовать название картинки перед сохранением
    """

    def _save(self, name, content):
        return super(SFTPFileSystemStorage, self)._save(name, content)
