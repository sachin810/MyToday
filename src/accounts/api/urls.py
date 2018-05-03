from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'accounts'

urlpatterns = [
    url(r'register/$', views.AccountCreateApiView.as_view(), name='index'),
    #url(r'logout/$', views.LogoutView, name='logout'),
    url(r'login/$', views.AccountLoginApiView.as_view(), name='login'),
    #url(r'profile/$', views.AccountUpdateView, name='profile'),

]