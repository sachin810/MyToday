from django import forms
from .models import Diary
from pagedown.widgets import PagedownWidget







class DiaryCreateForm(forms.ModelForm):

    title = forms.CharField(label='Title',widget=forms.TextInput(attrs={'size':65}))
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
 #   content = forms.CharField(
 #       widget=TinyMCEWidget(
 #           attrs={'required': False, 'cols': 30, 'rows': 10}
 #       )
 #   )


    class Meta:
        model = Diary
        fields = [
            'title',
            'content',
        ]