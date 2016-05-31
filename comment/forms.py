from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'product': forms.HiddenInput()
        }
