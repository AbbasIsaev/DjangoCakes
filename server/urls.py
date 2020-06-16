"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including anot her URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from photo import views as photo_views
from server.settings import STORAGE

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cake.urls')),
    path('favicon.ico', favicon_view),

    # Визуальный редактор, взято из https://pypi.org/project/django-ckeditor/#installation
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if STORAGE == 'SFTP':
    urlpatterns.append(path('media/<str:url>', photo_views.media_sftp))
elif STORAGE == 'WEBDAV':
    urlpatterns.append(path('media/<str:url>', photo_views.media_webdav))

# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
