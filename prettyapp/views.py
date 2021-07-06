import random

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, FormView

from prettyapp.forms import PrettyCreationForm
from prettyapp.models import PrettyModel


class PrettyCreationView(CreateView): #FormView도 생각해보기
    model = PrettyModel
    form_class = PrettyCreationForm
    template_name = 'photo.html'

    def get_success_url(self):
        return reverse('mainpage:mainpage')


class PrettyDetailView(DetailView): #FormView도 생각해보기
    model = PrettyModel
    context_object_name = 'target_pretty'
    template_name = 'photo_detail.html'

def random_pick(request):
    number = random.randrange(1, 5)
    return HttpResponseRedirect(reverse('prettyapp:photo_detail', args=[number]))
    #return render(request, '../pretty/photo_detail/number', {'number': number})

# class MaskCreationView(FormView):
#     form_class = MaskCreationForm
#     template_name = 'mask_create.html'
#
#     #form이 유효할때 바로 밑에 함수 실행
#     def form_valid(self, form):
#         searchword = form.cleaned_data['search_word']
#         user = User.objects.filter(Q(username__icontains=searchword))
#         context = {}
#         context['form'] = form
#         context['search_term'] = user
#
#         return render(self.request, self.template_name, context)