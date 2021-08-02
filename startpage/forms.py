
from django import forms
from django.forms import ModelForm

import accountapp
import startpage

# ModelChoiceField?
from startpage.models import WorldcupModel


class GameDetailForm(forms.Form):
    search_word = forms.FileField()


class WorldcupForm(ModelForm):
    class Meta:
        model = WorldcupModel
        fields = []
