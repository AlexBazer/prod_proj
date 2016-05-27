from django.forms import ModelForm
from like.models import Like


class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = '__all__'
