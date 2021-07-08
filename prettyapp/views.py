import random

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView, DeleteView, UpdateView

from prettyapp.forms import PrettyCreationForm
from prettyapp.models import PrettyModel, TestDataModel


class PrettyCreationView(CreateView): #FormView도 생각해보기
    model = PrettyModel
    form_class = PrettyCreationForm
    template_name = 'photo.html'

    def get_success_url(self):
        return reverse('mainpage:mainpage')


class PrettyDetailView(DetailView):  # FormView도 생각해보기
    model = PrettyModel
    #context_object_name = 'target_pretty'
    template_name = 'photo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PrettyDetailView, self).get_context_data(**kwargs)
        context['data_list'] = PrettyModel.objects.all()
        return context

class test_data(UpdateView):
    model = TestDataModel
    success_url = reverse_lazy('articleapp:list')
#class PrettyDeleteView(DeleteView):




# class PrettyDetailView(ListView): #FormView도 생각해보기
#     model = PrettyModel
#     context_object_name = 'target_pretty'
#     template_name = 'photo_detail.html'
#
#     number = random.randrange(1, 5)
#     number2 = random.randrange(1, 5)
#     context = {'number': number, 'number2': number2}
#
#     def get_context_object_name(self, object_list):
#
#     return render(self.request, self.template_name, context)

def random_pick(request):
    number = random.randrange(1, 5)
    #number2 = random.randrange(1, 5)

    #context = {'number': number, 'number2': number2}
    return HttpResponseRedirect(reverse('prettyapp:photo_detail', args=[number]))
    #return render(request, '../pretty/photo_detail/number', {'number': number})
    # return reverse(request, '../pretty/photo_detail', context)

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