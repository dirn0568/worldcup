from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse("헬로월드 1시간의 사투끝에 적음!")
