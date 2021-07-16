from django.urls import path

from subscribeapp.views import SubscriptionView, SubscribeListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscription/', SubscriptionView.as_view(), name='subscription'),
    path('subscribe_list', SubscribeListView.as_view(), name='subscribe_list'),
]
