# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms.widgets import Textarea


class AdminCodeMirrorWidget(Textarea):

    class Media:
        js = ['article_app/codemirror/lib/codemirror.js',
              'article_app/codemirror/addon/mode/overlay.js',
              'article_app/codemirror/mode/xml/xml.js',
              'article_app/codemirror/mode/markdown/markdown.js',
              'article_app/codemirror/mode/gfm/gfm.js',
              'article_app/codemirror/mode/javascript/javascript.js',
              'article_app/codemirror/mode/css/css.js',
              'article_app/codemirror/mode/htmlmixed/htmlmixed.js',
              'article_app/codemirror/mode/python/python.js',
              'article_app/codemirror/mode/shell/shell.js',
              'article_app/codemirror/mode/meta.js',
              'article_app/codemirror-lbe.js', ]
        css = {
            'all': ['article_app/codemirror/lib/codemirror.css',
                    'article_app/codemirror-lbe.css', ]
        }

    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs['class'] = attrs.setdefault('class', '') + ' codemirror-widget'
        super(AdminCodeMirrorWidget, self).__init__(attrs=attrs)
