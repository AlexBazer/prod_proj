from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from product.models import Product


class Comment(models.Model):
    message = models.TextField(_('Message'))
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        _('Created time'),
        default=timezone.now,
        blank=True,
        null=True
    )
    modified_at = models.DateTimeField(_('Modified time'), auto_now=True)

    def __str__(self):
        return 'comment for product "{0}" was added at {1}'.format(
            self.product.name,
            self.created_at
        )

    class Meta:
        ordering = ['-created_at', ]
