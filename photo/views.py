import mimetypes

from django.http import HttpResponse, Http404

from server.storage import SFTPFileSystemStorage, WebDavFileSystemStorage


def media_sftp(request, url):
    SFS = SFTPFileSystemStorage()

    if SFS.exists(url):
        file = SFS._read(url)
        type, encoding = mimetypes.guess_type(url)
        response = HttpResponse(file, content_type=type)
        response['Content-Disposition'] = u'attachment; filename="{filename}'.format(filename=url)
        return response
    raise Http404


def media_webdav(request, url):
    SFS = WebDavFileSystemStorage()

    if SFS.exists(url):
        file = SFS._open(url)
        type, encoding = mimetypes.guess_type(url)
        response = HttpResponse(file, content_type=type)
        response['Content-Disposition'] = u'attachment; filename="{filename}'.format(filename=url)
        return response
    raise Http404
