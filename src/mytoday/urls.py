
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/', include('diary.urls')),
    path('', include('accounts.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/diary/', include('diary.api.urls')),

]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)