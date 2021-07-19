from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='빠른 검색',
                                  widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                'autocomplete': 'off',
                                                                'size': '40',
                                                                'style': 'font-size: x-large',
                                                                }))

class PostDetailForm(forms.Form):
    search_word = forms.CharField(label='빠른 검색',
                                  widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                'autocomplete': 'off',
                                                                'size': '40',
                                                                'style': 'font-size: x-large',
                                                                }))


