from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _


class Comment(models.Model):
    message = models.TextField(_('Message'))
    created_at = models.DateTimeField(_('Created time'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modified time'), auto_now=True)
