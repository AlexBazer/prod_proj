from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class ProductsTest(TestCase):
    fixtures = ['products.json', ]

    def setUp(self):
        self.client = Client()

    def test_(self):
        response = self.client.get(reverse('product:index'))
        self.assertEqual(response.status_code, 200)
