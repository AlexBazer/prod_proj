from django.conf.urls import url
from product.views import Products, ProductItem


urlpatterns = [
    url(r'^products/$', Products.as_view(), name='index'),
    url(r'^products/(?P<slug>[-\w]+)$', ProductItem.as_view(), name='product_item')
]
