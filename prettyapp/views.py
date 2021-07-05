from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from prettyapp.forms import PrettyCreationForm
from prettyapp.models import PrettyModel


class PrettyCreationView(CreateView): #FormView도 생각해보기
    model = PrettyModel
    form_class = PrettyCreationForm
    template_name = 'photo.html'

    def get_success_url(self):
        return reverse('mainpage:mainpage')


class PrettyDetailView(DetailView): #FormView도 생각해보기
    model = PrettyModel
    context_object_name = 'target_pretty'
    template_name = 'photo_detail.html'