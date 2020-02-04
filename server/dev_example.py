from server.settings import STORAGE, STORAGE_DIR

if STORAGE == 'SFTP':
    # Подключение к удаленному SFTP серверу
    SFTP_STORAGE_HOST = '127.0.0.1'
    SFTP_STORAGE_ROOT = '/media/' + STORAGE_DIR
    SFTP_STORAGE_PARAMS = {
        'username': 'username',
        'password': 'password',
        'allow_agent': False,
        'look_for_keys': False,
    }
    SFTP_STORAGE_INTERACTIVE = False
elif STORAGE == 'WEBDAV':
    # Подключение к удаленному Webdav серверу
    WEBDAV_URL = 'https://username:password@webdav.yandex.ru'
    WEBDAV_PUBLIC_URL = "/media/"
