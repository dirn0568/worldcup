from django.shortcuts import render

# Create your views here.

def end_game(request):
    return render(request, 'endpage.html')