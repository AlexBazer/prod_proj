from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'), max_length=100)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(_('Created time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modified time'), auto_now=True)

    def __unicode__(self):
        return self.name
