from __future__ import unicode_literals
from django import forms
from django.utils.translation import gettext as _

from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'product']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'product': forms.HiddenInput()
        }
        error_messages = {
            'message': {
                'required': _("Message can not be empty"),
            },
        }
