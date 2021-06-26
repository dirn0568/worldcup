from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def login_page(request):
    return render(request, 'login.html')

# def login_system(request):

