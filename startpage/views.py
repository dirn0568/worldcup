from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView

from startpage.forms import GameDetailForm


def play(request):

    #def get_success_url(self):

    return render(request, 'play.html')

def test2(request):

    #def get_success_url(self):

    return render(request, 'test2.html')

def test5(request):

    #def get_success_url(self):

    return render(request, 'test5.html')

class GameDetailView(FormView):
    form_class = GameDetailForm
    template_name = 'game_test.html'

    #form이 유효할때 바로 밑에 함수 실행
    def form_valid(self, form):
        choice_img = form.cleaned_data['choice']
        # user = User.objects.filter(Q(username__icontains=searchword))
        context = {}
        context['img'] = "../static/bg04.png"
        context['choice'] = choice_img

        return render(self.request, self.template_name, context)