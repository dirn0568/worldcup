from django.forms import ModelForm

from django import forms
from prettyapp.models import PrettyModel


class PrettyCreationForm(ModelForm):
    class Meta:
        model = PrettyModel
        fields = ['image', 'title', 'nickname']


# class MaskCreationForm(forms.Form):
#     image = forms.ImageField(upload_to='pretty/', null=True, label='image')
#     title = forms.CharField(max_length=20, null=False, label='title')
#     nickname = forms.CharField(max_length=20, unique=True, null=True, label='nickname')

    # def __str__(self):
    #     return f'{self.pk} : {self.title}'