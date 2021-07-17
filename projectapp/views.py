from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView, UpdateView, DeleteView

from articleapp.forms import ArticleCreateForm
from articleapp.models import ArticleCreateModel
from commentapp.forms import CommentForms
from mainpage.forms import PostSearchForm
from projectapp.forms import ProjectCreateForm, ProjectUpdateForm
from projectapp.models import ProjectCreateModel
from subscribeapp.models import SubscribeCreateModel


class ProjectCreateView(CreateView):
    model = ProjectCreateModel
    form_class = ProjectCreateForm
    template_name = 'project_create.html'

    def form_valid(self, form):
        temp_project = form.save(commit=False)
        temp_project.project = self.request.user
        temp_project.save()
        return super().form_valid(form)

class ProjectListView(ListView, FormView):
    model = ProjectCreateModel
    form_class = PostSearchForm
    context_object_name = 'target_project'
    template_name = 'project_list.html'

    paginate_by = 5

class ProjectDetailView(DetailView, FormView):
    model = ProjectCreateModel
    form_class = ArticleCreateForm
    context_object_name = 'target_project_detail'
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        object_list = ArticleCreateModel.objects.filter(article_project=self.get_object())
        print(self.object, '##########################')
        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = SubscribeCreateModel.objects.filter(subscribe_project=project, subscribe_user=user)
        else:
            subscription = None

        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)

class ProjectUpdateView(UpdateView):
    model = ProjectCreateModel
    form_class = ProjectUpdateForm
    success_url = reverse_lazy('mainpage:mainpage')
    context_object_name = 'target_project_update'
    template_name = 'project_update.html'

class ProjectDeleteView(DeleteView):
    model = ProjectCreateModel
    context_object_name = 'target_project_delete'
    success_url = reverse_lazy('mainpage:mainpage')
    template_name = 'project_delete.html'


class ProjectArticleView(DetailView, FormView):
    model = ProjectCreateModel
    form_class = ArticleCreateForm
    context_object_name = 'target_project_article'
    template_name = 'project_article_create.html'

    def form_valid(self, form):
        print('실행됨?')
        print(self.request.user)
        print(self.request.POST['project_pk'])
        temp_article = form.save(commit=False)
        temp_article.article = self.request.user
        # temp_article.article_project = ProjectCreateModel.objects.get(pk=self.request.pk)
        temp_article.article_project = ProjectCreateModel.objects.get(pk=self.request.POST['project_pk'])
        temp_article.save()
        return super().form_valid(form)

class ProjectSearchForm(FormView):
    form_class = PostSearchForm
    template_name = 'project_list.html'

    def form_valid(self, form):
        searchword = form.cleaned_data['search_word']
        user = User.objects.filter(username=searchword)

        for entp in user:
            return HttpResponseRedirect(reverse('accountapp:detail', args=[entp.pk]))





