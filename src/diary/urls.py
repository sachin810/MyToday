from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'diary'

urlpatterns = [
    url(r'^$', views.DiaryListView, name='index'),
    url(r'(?P<slug>[\w-]+)/$', views.DiaryDetailView, name='detail'),
    #    url(r'^$',views.DiaryCreateView,name='create')
    url(r'(?P<pk>\d+)/edit$', views.DiaryUpdateView, name='edit'),
    url(r'(?P<pk>\d+)/delete', views.DiaryDeleteView, name='delete'),

]