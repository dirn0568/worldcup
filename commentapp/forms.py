from django import forms
from django.forms import ModelForm

from commentapp import models
from commentapp.models import CommentModel

# class CommentForm(forms.Form):
#     comment_word = forms.CharField(label='text')

class CommentForms(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment_text']

class CommentUpdateForm(CommentForms):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)