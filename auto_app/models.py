from __future__ import unicode_literals

from django.db import models


class AutoModel(models.Model):
    model_name = models.CharField(max_length=255)
    generation = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
