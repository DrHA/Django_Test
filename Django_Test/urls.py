"""Django_Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cmdb import views

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
   url(r'^index/servers', views.servers),
   url(r'^index/mails', views.mails),
   url(r'^index/config', views.config),
   url(r'^index/log', views.log),
   url(r'^index/scripts', views.scripts),
   url(r'^index/server_list', views.server_list),
   url(r'^index/main', views.main),
   url(r'^index/user_list', views.user_list),
   url(r'^main/', views.main),
   url(r'^sign/', views.sign),
   url(r'^index/', views.index),
   url(r'^$', views.index),
]
