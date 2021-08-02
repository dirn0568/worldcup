from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import FormView, CreateView, RedirectView, DetailView

from startpage.forms import GameDetailForm, WorldcupForm
from startpage.models import WorldcupModel


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


def GameTetrisView(request):

    return render(request, 'tetris.html')

def GameWorldcupView(request):

    return render(request, 'worldcup.html')


def GameWorldcupEndView(request):
    print('되는중?/11!?!?!?!?!?!?!?!?!?!?!!11111111')
    print(WorldcupModel)
    print(WorldcupModel.objects[0])
    loke = WorldcupModel.objects.filter(like_1=0)
    context = {'loke' : loke}
    print(loke)
    return render(request, 'worldcup_end.html', context)

# class DetailWorldcup(DetailView):
#     model = WorldcupModel
#     context_object_name = 'target_worldcup'

class CreateWorldcup(CreateView):
    model = WorldcupModel
    form_class = WorldcupForm
    context_object_name = 'target_worldcup'
    template_name = 'worldcup_create.html'

    # def get_redirect_url(self, context_object_name):
    #     print('실행중?11111111111111111')
    #     return reverse('game:worldcup_end')
    def get_success_url(self, context_object_name):
        return reverse('game:worldcup_end')

# class WorldcupClass(View):
#     model = WorldcupModel