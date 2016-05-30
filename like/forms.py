from django import forms
from like.models import Like


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'product': forms.HiddenInput()
        }
