import os

from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp import views


def initial_page(request):
    # if request.method == 'POST':
    #     print("이거 나옴?")
    #     a = request.POST.getlist("datas")
    #     print(a)
    #     return render(request, views.test_page, [a])
    return render(request, 'basic.html')