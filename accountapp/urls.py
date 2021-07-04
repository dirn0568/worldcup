from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp import views
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, \
    ProfileCreateView, ProfileUpdateView

app_name = "accountapp"

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

    path('profile_create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profile_update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


]