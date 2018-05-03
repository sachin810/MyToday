from django.contrib import admin
from .models import Diary


class DiaryModelAdmin(admin.ModelAdmin):
    list_display = ['timestamp']
    class Meta:
        model = Diary

admin.site.register(Diary, DiaryModelAdmin)


