from django.shortcuts import render

# Create your views here.
from django.urls import reverse

def play(request):
    return render(request, 'play.html')
