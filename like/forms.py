from django import forms
from like.models import Like


class LikeForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput())
    product = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Like
        fields = '__all__'
