from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, TemplateView

from product.models import Product
from comment.models import Comment
from like.models import Like
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
        """Populate context

        Add CommentForm, LikeForm, comments, like counter, can_like to  the context
        """

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
        context['comments'] = Comment.objects.filter(product=self.object)

        context['likes_count'] = Like.objects.filter(product=self.object).count()

        context['can_like'] = (
            self.request.user.is_authenticated() and
            Like.objects.filter(product=self.object, user=self.request.user)
        )

        return context

    def post(self, request, slug):
        """Handle Like and Comment forms"""

        context = self.get_context_data()

        # Forms with template names than can be handled
        # (<form name>, <formClass>, <login pass flag>)
        forms = [
            ('form_comment', CommentForm, True),
            ('form_like', LikeForm, request.user.is_authenticated())
        ]

        # go through forms and handle one in post was from it
        for form_name, form, login_pass in forms:
            if form_name not in request.POST or not login_pass:
                continue
            context[form_name] = form(request.POST)
            if context[form_name].is_valid():
                context[form_name].save()
                return redirect('product:product_item', slug=self.object.slug)
            return render(request, self.template_name, context)

        return self.http_method_not_allowed(request)
