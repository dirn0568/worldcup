from django.contrib.auth.views import LoginView
from django.urls import path

from accountapp import views
from accountapp.views import AccountCreateView, AccountDetailView

app_name = "accountapp"

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/', AccountDetailView.as_view(), name='detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),


]