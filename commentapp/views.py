from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DetailView

from articleapp.models import ArticleCreateModel
from commentapp.forms import CommentForms
from commentapp.models import CommentModel


class CommentView(CreateView):
    model = CommentModel
    form_class = CommentForms
    success_url = reverse_lazy('mainpage:mainpage')
    template_name = 'comment.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.writer = ArticleCreateModel.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.save()
        return super().form_valid(form)
