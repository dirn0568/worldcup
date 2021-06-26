from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def initial_page(request):
    return render(request, 'basic.html')
    # return HttpResponse("헬로월드 1시간의 사투끝에 적음!")
