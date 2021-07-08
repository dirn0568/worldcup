
from django import forms

import accountapp
import startpage

# ModelChoiceField?
class GameDetailForm(forms.Form):
    search_word = forms.FileField()