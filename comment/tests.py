from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from product.models import Product


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
