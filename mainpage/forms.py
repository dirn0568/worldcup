from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='빠른 검색')

class PostDetailForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
