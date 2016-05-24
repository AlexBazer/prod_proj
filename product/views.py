from django.shortcuts import render
from django.views.generic import View, ListView

from product.models import Product


class Products(ListView):
    template_name = 'product/products.html'
    model = Product
    paginate_by = 10
