from django.conf.urls import patterns, url
from product.views import Products


urlpatterns = patterns(
    '',
    url(r'products/', Products.as_view())
)
