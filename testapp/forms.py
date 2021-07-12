from django.forms import ModelForm

from commentapp.models import CommentModel


class CommentForms(ModelForm):
    class Meta:
        model = CommentModel