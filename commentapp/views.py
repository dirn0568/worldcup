from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, DetailView, DeleteView, UpdateView

from accountapp.models import Profile
from articleapp.models import ArticleCreateModel
from commentapp.forms import CommentForms, CommentUpdateForm
from commentapp.models import CommentModel


class CommentView(CreateView):
    model = CommentModel
    form_class = CommentForms
    success_url = reverse_lazy('mainpage:mainpage')
    template_name = 'comment.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.writer = ArticleCreateModel.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer_nickname = Profile.objects.get(pk=self.request.user.profile.pk)
        temp_comment.save()
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = CommentModel
    context_object_name = 'target_comment'
    form_class = CommentUpdateForm
    #success_url = reverse_lazy('mainpage:mainpage')
    template_name = 'comment_update.html'

    def get_success_url(self):
        print('####################')
        print(self.object)
        print(self.object.writer.article_title)
        print(self.object.writer.article)
        return reverse('articleapp:article_detail', kwargs={'pk': self.object.writer.pk})

class CommentDeleteView(DeleteView):
    model = CommentModel
    context_object_name = 'target_comment'
    success_url = reverse_lazy('mainpage:mainpage')
    template_name = 'comment_delete.html'

