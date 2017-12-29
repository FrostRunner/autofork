from __future__ import unicode_literals

# -*- coding: utf-8 -*-
"""autofork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    path(r'', include(('article_app.urls', 'article_app'))),
]


"""
module – URLconf module (or module name)
namespace (string) – Instance namespace for the URL entries being included
pattern_list – Iterable of path() and/or re_path() instances.
app_namespace (string) – Application namespace for the URL entries being included
"""

handler404 = 'article_app.views.e404'
