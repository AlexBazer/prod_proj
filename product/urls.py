from django.conf.urls import url
from product.views import Products


urlpatterns = [
    url(r'products/', Products.as_view(), name='index')
]
