"""worldcup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('mainpage.urls')),
    path('play/', include('startpage.urls')),
    path('endpage/', include('endpage.urls')),
    path('loginpage/', include('accountapp.urls')),
    path('pretty/', include('prettyapp.urls')),
    path('article/', include('articleapp.urls')),
    path('comment/', include('commentapp.urls')),
    path('project/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
    path('like/', include('likeapp.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # static, settings.MEDIA_URL, document_root 다 뭔 뜻임
