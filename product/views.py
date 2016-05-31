from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, ListView, DetailView, TemplateView
from django.utils.translation import gettext as _

from product.models import Product
from comment.models import Comment
from like.models import Like
from comment.forms import CommentForm
from like.forms import LikeForm

from collections import namedtuple

""" Form handler to be user with other forms in one view

    attribures:
    name: form name
    form: form object
    template_form: initiated form object
    auth_pass: can be user to disable form processing
    success_msg: message ufter form submission
"""
ViewForm = namedtuple('ViewForm', (
    'name',
    'form',
    'auth_pass',
    'success_msg'
))

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

        self.forms = {
            'form_comment': ViewForm(
                name='form_comment',
                form=CommentForm,
                auth_pass=True,
                success_msg=_('Comment was successfully added')
            ),
            'form_like': ViewForm(
                name='form_like',
                form=LikeForm,
                auth_pass=self.request.user.is_authenticated(),
                success_msg=_("You've liked this product")
            )
        }
        context['form_comment'] = self.forms['form_comment'].form(initial={'product': self.object.id})
        context['form_like'] = self.forms['form_like'].form(initial={
            'user': self.request.user.id, 'product': self.object.id}
        )

        context['comments'] = Comment.objects.filter(product=self.object)

        context['likes_count'] = Like.objects.filter(product=self.object).count()

        context['can_like'] = (
            self.request.user.is_authenticated() and
            not Like.objects.filter(product=self.object, user=self.request.user)
        )

        return context

    def post(self, request, slug):
        """Handle Like and Comment forms"""

        context = self.get_context_data()

        # go through forms and handle one in post was from it
        for viewForm in self.forms.values():
            if viewForm.name not in request.POST or not viewForm.auth_pass:
                continue
            context[viewForm.name] = viewForm.form(request.POST)
            if context[viewForm.name].is_valid():
                context[viewForm.name].save()
                messages.info(request, viewForm.success_msg)
                return redirect('product:product_item', slug=self.object.slug)
            return render(request, self.template_name, context)

        return self.http_method_not_allowed(request)
