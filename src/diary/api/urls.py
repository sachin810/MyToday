from . import views
from django.conf.urls import url


app_name = 'diary-api'


urlpatterns = [
    url(r'^create/$', views.DiaryCreateApiView.as_view(), name='create'),
    url(r'^$', views.DiaryListApiView.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.DiaryDetailApiView.as_view(), name='detail'),
    url(r'(?P<slug>[\w-]+)/edit$', views.DiaryUpdateApiView.as_view(), name='edit'),
    url(r'(?P<slug>[\w-]+)/delete', views.DeleteDiaryApiView.as_view(), name='delete'),

]

