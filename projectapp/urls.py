from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from projectapp.views import ProjectCreateView, ProjectListView, ProjectDetailView, ProjectArticleView

app_name = 'projectapp'

urlpatterns = [
    path('project_create', ProjectCreateView.as_view(), name='project_create'),
    path('project_list', ProjectListView.as_view(), name='project_list'),

    path('project_detail/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),

    path('project_article_create/<int:pk>', ProjectArticleView.as_view(), name='project_article_create'),
]
