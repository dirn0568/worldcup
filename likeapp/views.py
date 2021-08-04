from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView

from articleapp.models import ArticleCreateModel
from likeapp.models import LikeRecordModel


@transaction.atomic
def db_transaction(user, article):

    if LikeRecordModel.objects.filter(user=user, article=article).exists():
        print('실행중?333333333333333333')
        raise ValidationError('Like already exists')
    else:
        LikeRecordModel(user=user, article=article).save()
    article.like += 1
    article.save()

class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        print('실행중?11111111111111111')
        return reverse('articleapp:article_detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):
        print('실행중?22222222222222')
        user = self.request.user
        print(args, '####################################')
        article = get_object_or_404(ArticleCreateModel, pk=kwargs['pk'])

        try:
            db_transaction(user, article)
            messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')
        except ValidationError:
            messages.add_message(self.request, messages.ERROR, '좋아요는 한번만 가능합니다.')
            return HttpResponseRedirect(reverse('articleapp:article_detail', kwargs={'pk': kwargs['pk']}))

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)