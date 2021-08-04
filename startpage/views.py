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

    def form_valid(self, form):
        temp_worldcup = form.save(commit=False)
        temp_worldcup.like_8 += 3
        temp_worldcup.save()
        return super().form_valid(form)

    def get_success_url(self):
        print(self.object, '2131231241251512')
        return reverse('game:worldcup_detail', kwargs={'pk': self.object.pk})

    # def get_redirect_url(self, context_object_name):
    #     print('실행중?11111111111111111')
    #     return reverse('game:worldcup_end')
    # def get_success_url(self, context_object_name):
    #     return reverse('game:worldcup_end')

class DetailWorldcup(DetailView):
    model = WorldcupModel
    context_object_name = 'target_worldcup'
    template_name = 'worldcup_detail.html'

# class WorldcupClass(View):
#     model = WorldcupModel

# class rwyrwywView(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         return reverse('articleapp:article_detail', kwargs={'pk': kwargs['pk']})
#
#     def get(self, *args, **kwargs):
#         user = self.request.user
#         article = get_object_or_404(ArticleCreateModel, pk=kwargs['pk'])
#
#         try:
#             db_transaction(user, article)
#             messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')
#         except ValidationError:
#             return HttpResponseRedirect(reverse('articleapp:article_detail', kwargs={'pk': kwargs['pk']}))
#
#         return super(LikeArticleView, self).get(self.request, *args, **kwargs)

def testing555(request, number):
    print(WorldcupModel.objects)
    loke = WorldcupModel.objects.filter(pk=1)
    print(number)
    print(loke)
    # print(loke.like_1)
    for intp in loke:
        print(intp)
        print(intp.like_1)
        intp.like_1 += 1
        if number == 1:
            print('이거 작동안돼1?')
            intp.like_1 += 1
        elif number == 2:
            print('이거 작동안돼?2')
            intp.like_2 += 1
        elif number == 3:
            print('이거 작동안돼?3')
            intp.like_3 += 1
        elif number == 4:
            print('이거 작동안돼?4')
            intp.like_4 += 1
        elif number == 5:
            print('이거 작동안돼?5')
            intp.like_5 += 1
        elif number == 6:
            print('이거 작동안돼?6')
            intp.like_6 += 1
        elif number == 7:
            print('이거 작동안돼?7')
            intp.like_7 += 1
        elif number == 8:
            print('이거 작동안돼?8')
            intp.like_8 += 1
        intp.save()
        context = {'loke': intp}
    return render(request, 'worldcup_end.html', context)