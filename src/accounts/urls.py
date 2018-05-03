from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.RegisterView, name='index'),
    url(r'logout/$', views.LogoutView, name='logout'),
    url(r'login/$', views.LoginView, name='login'),
    url(r'profile/$', views.AccountUpdateView, name='profile'),

]