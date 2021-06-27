from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def initial_page(request):
    if request.method == 'POST':
        print("이거 나옴?")
        a = request.POST.getlist("data")
        print(a)
        return render(request, 'endpage.html', {"data": a})
    return render(request, 'basic.html')
    # return HttpResponse("헬로월드 1시간의 사투끝에 적음!")
