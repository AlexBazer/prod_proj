from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, TemplateView

from product.models import Product
from comment.forms import CommentForm
from like.forms import LikeForm


class Products(ListView):
    template_name = 'product/products.html'
    model = Product
    paginate_by = 10


class ProductItem(DetailView):
    template_name = 'product/product_item.html'
    model = Product

    def get_context_data(self, **kwargs):
        """Add  CommentForm and LikeForm to context"""

        self.object = self.get_object()
        context = super(ProductItem, self).get_context_data(**kwargs)
        context['form_comment'] = CommentForm(
            initial={
                'product': self.object.id
            }
        )
        context['form_like'] = LikeForm(
            initial={
                'user': self.request.user.id,
                'product': self.object.id
            }
        )

        return context

    def post(self, request, slug):
        """Handle Like and Comment forms"""

        context = self.get_context_data()
        form_names = [
            ('form_comment', CommentForm),
            ('form_like', LikeForm)
        ]

        for form_name, form in form_names:
            if form_name not in request.POST:
                continue
            context[form_name] = form(request.POST)
            if context[form_name].is_valid():
                return redirect('product:product_item', slug=self.object.slug)
            return render(request, self.template_name, context)

        return self.http_method_not_allowed(request)
