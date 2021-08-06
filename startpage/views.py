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


class DetailWorldcup(DetailView):
    model = WorldcupModel
    context_object_name = 'target_worldcup'
    template_name = 'worldcup_detail.html'


def testing555(request, number):
    loke = WorldcupModel.objects.filter(pk=5)
    for intp in loke:
        if number == '001.webm':
            print('이거 작동안돼1?')
            intp.like_1 += 1
            img_name = 'meteo'
        elif number == '002.webm':
            print('이거 작동안돼?2')
            intp.like_2 += 1
            img_name = 'VVS'
        elif number == '003.webm':
            print('이거 작동안돼?3')
            intp.like_3 += 1
            img_name = '밝게 빛나는 별이되어'
        elif number == '004.webm':
            print('이거 작동안돼?4')
            intp.like_4 += 1
            img_name = '오래된 노래'
        elif number == '005.mp4':
            print('이거 작동안돼?5')
            intp.like_5 += 1
            img_name = 'blue'
        elif number == '006.mp4':
            print('이거 작동안돼?6')
            intp.like_6 += 1
            img_name = '하루하루'
        elif number == '007.mp4':
            print('이거 작동안돼?7')
            intp.like_7 += 1
            img_name = 'shape of you'
        elif number == '008.mp4':
            print('이거 작동안돼?8')
            intp.like_8 += 1
            img_name = 'Counting Stars'
        intp.save()
        zerotwo = intp.like_1 + intp.like_2 + intp.like_3 + intp.like_4 + intp.like_5 + intp.like_6 + intp.like_7 + intp.like_8
        winner1 = round(intp.like_1 / zerotwo * 100, 1)
        winner2 = round(intp.like_2 / zerotwo * 100, 1)
        winner3 = round(intp.like_3 / zerotwo * 100, 1)
        winner4 = round(intp.like_4 / zerotwo * 100, 1)
        winner5 = round(intp.like_5 / zerotwo * 100, 1)
        winner6 = round(intp.like_6 / zerotwo * 100, 1)
        winner7 = round(intp.like_7 / zerotwo * 100, 1)
        winner8 = round(intp.like_8 / zerotwo * 100, 1)
        winner_list = [winner1, winner2, winner3, winner4, winner5, winner6, winner7, winner8]
        winner_list2 = {intp.like_1:['메테오','001.webm'],
                        intp.like_2:['VVS','002.webm'],
                        intp.like_3:['밝게빛나는별이되어','003.webm'],
                        intp.like_4:['오래된 노래','004.webm'],
                        intp.like_5:['blue','005.mp4'],
                        intp.like_6:['하루하루','006.mp4'],
                        intp.like_7:['shape of you','007.mp4'],
                        intp.like_8:['Counting Stars','008.mp4']}
        winner_list3 = [intp.like_1, intp.like_2, intp.like_3, intp.like_4, intp.like_5, intp.like_6, intp.like_7, intp.like_8]
        winner_list.sort()
        winner_list.reverse()
        winner_list3.sort()
        winner_list3.reverse()
        context = {'loke': intp,
                   'winner1' : winner1,
                   'winner2' : winner2,
                   'winner3' : winner3,
                   'winner4' : winner4,
                   'winner5' : winner5,
                   'winner6' : winner6,
                   'winner7' : winner7,
                   'winner8' : winner8,
                   'zerotwo' : zerotwo,
                   'win1': winner_list2[winner_list3[0]][0],
                   'win2': winner_list2[winner_list3[1]][0],
                   'win3': winner_list2[winner_list3[2]][0],
                   'win4': winner_list2[winner_list3[3]][0],
                   'win5': winner_list2[winner_list3[4]][0],
                   'win6': winner_list2[winner_list3[5]][0],
                   'win7': winner_list2[winner_list3[6]][0],
                   'win8': winner_list2[winner_list3[7]][0],
                   'img' : number,
                   'img_name': img_name,
                   'img1' : winner_list2[winner_list3[0]][1],
                   'img2' : winner_list2[winner_list3[1]][1],
                   'img3' : winner_list2[winner_list3[2]][1],
                   'img4' : winner_list2[winner_list3[3]][1],
                   'img5' : winner_list2[winner_list3[4]][1],
                   'img6' : winner_list2[winner_list3[5]][1],
                   'img7' : winner_list2[winner_list3[6]][1],
                   'img8' : winner_list2[winner_list3[7]][1],
                   'winner_list' : winner_list,
                   'winner_list2' : winner_list2,
                   'winner_list3' : winner_list3 }
    return render(request, 'worldcup_end.html', context)