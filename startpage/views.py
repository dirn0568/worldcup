from django.shortcuts import render

# Create your views here.
from django.urls import reverse

def play(request):

    #def get_success_url(self):

    return render(request, 'play.html')
