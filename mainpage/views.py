import os

from django.contrib.auth.models import User
from django.forms import forms
from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView

from accountapp import views
from mainpage.forms import PostSearchForm


def initial_page(request):
    # if request.method == 'POST':
    #     print("이거 나옴?")
    #     a = request.POST.getlist("datas")
    #     print(a)
    #     return render(request, views.test_page, [a])
    return render(request, 'basic.html')

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'search.html'

    # def get_success_url(self):
    def form_valid(self, form):
        searchword = form.cleaned_data['search_word']
        user = User.objects.filter(username=searchword)
        context = {}
        context['form'] = form
        context['search_term'] = user
        return render(self.request, self.template_name, context)
