from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class ProductsTest(TestCase):
    fixtures = ['products.json', ]

    def setUp(self):
        self.client = Client()

    def test_products_page(self):
        response = self.client.get(reverse('product:index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/products.html')
        self.assertEqual(len(response.context['object_list']), 10)
