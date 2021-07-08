from django.forms import ModelForm

from articleapp import models
from articleapp.models import ArticleCreateModel


class ArticleCreateForm(ModelForm):
    class Meta:
        model = ArticleCreateModel
        fields = ['article_img', 'article_title', 'article_text']