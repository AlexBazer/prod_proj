from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.utils import timezone

from datetime import timedelta

from product.models import Product
from comment.models import Comment


class ProductsTest(TestCase):
    fixtures = ['products.json', ]

    def setUp(self):
        self.client = Client()

    def test_comment_add(self):
        msg = 'Here is the message'
        product = Product.objects.first()

        response = self.client.post(reverse('product:product_item', kwargs={'slug': product.slug}), {
            'message': msg,
            'product': product.id,
            'form_comment': ''
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_item.html')
        self.assertIn(msg, response.content)

    def test_comment_old(self):
        msg = 'Here is the message too old'
        product = Product.objects.first()
        comment = Comment.objects.create(
            message=msg,
            product=product,
            created_at=(timezone.now() - timedelta(days=2))
        )
        response = self.client.get(reverse('product:product_item', kwargs={'slug': product.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_item.html')
        self.assertNotIn(msg, response.content)
