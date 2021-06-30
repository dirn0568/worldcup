from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template.context_processors import request


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)