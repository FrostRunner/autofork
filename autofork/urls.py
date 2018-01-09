# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path(r'ckeditor/', include('ckeditor_uploader.urls')),
                  path(r'', include(('article_app.urls', 'article_app'))),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'article_app.views.e404'
