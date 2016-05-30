from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from product.models import Product
from like.forms import LikeForm


class ProductsTest(TestCase):
    fixtures = ['products.json', ]

    def setUp(self):
        self.user_pass = 'test'
        self.user = User.objects.create_user(
            username='test',
            password=self.user_pass
        )
        self.client = Client()

    def test_like_anonymous(self):
        product = Product.objects.first()
        response = self.client.post(reverse('product:product_item', kwargs={'slug': product.slug}), {
            'product': product.id,
            'user': self.user.id,
            'form_like': ''
        }, follow=True)

        self.assertEqual(response.status_code, 405)

    def test_like_user(self):
        product = Product.objects.first()
        self.client.login(
            username=self.user.username,
            password=self.user_pass
        )
        # Users firs try to like!
        response = self.client.post(reverse('product:product_item', kwargs={'slug': product.slug}), {
            'product': product.id,
            'user': self.user.id,
            'form_like': ''
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_item.html')
        self.assertEqual(1, response.context['likes_count'])

        # if we wont to wote second time!
        response = self.client.post(reverse('product:product_item', kwargs={'slug': product.slug}), {
            'product': product.id,
            'user': self.user.id,
            'form_like': ''
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Like with this User and Product already exists.', response.context['form_like'].errors['__all__'])
