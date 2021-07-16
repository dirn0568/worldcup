
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView, ListView, FormView, DetailView
from django.views.generic.list import MultipleObjectMixin

from articleapp.forms import ArticleCreateForm
from articleapp.models import ArticleCreateModel
from projectapp.models import ProjectCreateModel
from subscribeapp.models import SubscribeCreateModel


class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:project_detail', kwargs={'pk': self.request.GET.get('project_pk')})


    def get(self, request, *args, **kwargs):
        project = get_object_or_404(ProjectCreateModel, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = SubscribeCreateModel.objects.filter(subscribe_user=user,
                                                           subscribe_project=project)

        if subscription.exists():
            subscription.delete()
            print("실행중?@2222222222222222")
        else:
            SubscribeCreateModel(subscribe_user=user, subscribe_project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)


# 희안하게 이건 에러가 있음 왜 있는지 모르겠음 바로 아래 문장(필요없는 문장임)#
# class SubscribeListView(ListView):
#     model = SubscribeCreateModel
#     context_object_name = 'article_subscribe'
#     template_name = 'subscribe_list.html'

class SubscribeListView(ListView):
    model = ArticleCreateModel
    context_object_name = 'article_subscribe'
    template_name = 'subscribe_list.html'

    def get_queryset(self):
        projects = SubscribeCreateModel.objects.filter(subscribe_user=self.request.user).values_list('subscribe_project')
        article_subscribe = ArticleCreateModel.objects.filter(article_project__in=projects)
        return article_subscribe

