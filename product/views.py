from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from product.models import Product


class Products(ListView):
    template_name = 'product/products.html'
    model = Product
    paginate_by = 10


class ProductItem(DetailView):
    template_name = 'product/product_item.html'
    model = Product
