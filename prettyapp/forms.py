from django.forms import ModelForm

from prettyapp.models import PrettyModel


class PrettyCreationForm(ModelForm):
    class Meta:
        model = PrettyModel
        fields = ['image', 'title', 'nickname']