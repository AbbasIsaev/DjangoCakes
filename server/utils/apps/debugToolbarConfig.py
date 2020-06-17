# Панель отладки Django, взято из https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

DEBUG_TOOLBAR_APPS = [
    'debug_toolbar'
]

DEBUG_TOOLBAR_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = [
    '127.0.0.1'
]
