import os

from django.contrib.auth.models import User
from django.forms import forms
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView

from accountapp import views
from mainpage.forms import PostSearchForm, PostDetailForm


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'basic.html'

    def form_valid(self, form):
        searchword = form.cleaned_data['search_word']
        user = User.objects.filter(username=searchword)

        for entp in user:
            return HttpResponseRedirect(reverse('accountapp:detail', args=[entp.pk]))
            # kwargs, args 둘다 가능, 하지만 두개를 같이 쓰는건 불가능, reverse만 써도 불가능 HRR이 같이 있어야함
            # HttpResponseRedirect 지정된 url로 redirect할때 사용
            # render는 템플릿을 불러오면서 내용을 전달할 수 있는 함수, redirect는 url 그 자체로 이동
            # return HttpResponseRedirect(reverse('accountapp:detail', kwargs={'pk': entp.pk}))

class SearchDetailView(FormView):
    form_class = PostDetailForm
    template_name = 'search.html'

    #form이 유효할때 바로 밑에 함수 실행
    def form_valid(self, form):
        searchword = form.cleaned_data['search_word']
        user = User.objects.filter(username=searchword)
        context = {}
        context['form'] = form
        context['search_term'] = user
        return render(self.request, self.template_name, context)

