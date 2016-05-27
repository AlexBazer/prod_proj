from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Like(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)

    class Meta():
        unique_together = (('user', 'product'),)
