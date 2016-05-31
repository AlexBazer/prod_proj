from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    def __unicode__(self):
        return 'use {username} likes "{product_name}"'.format(
            username=self.user.username,
            product_name=self.product.name
        )

    class Meta():
        unique_together = (('user', 'product'),)
