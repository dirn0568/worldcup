from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.http import HttpResponse
from django.template.context_processors import request

from accountapp.models import Profile


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProfileCreationForm(ModelForm):
    #class Meta를 써야 모델폼으로써 구실을 할수있음 class meta를 이용해서 커스터마이징할수있는거 같음
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']

class ProfileUpdateForm(ProfileCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)