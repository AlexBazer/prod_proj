from django.shortcuts import render
from django.views.generic import View


class Products(View):
    template_name = 'product/products.html'

    def get(self, request):
        return render(request, self.template_name)
