from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView

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



