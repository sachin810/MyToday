from diary.models import Diary
from rest_framework import serializers


class DiaryListSerailizer(serializers.ModelSerializer):

    url =serializers.HyperlinkedIdentityField(view_name='diary-api:detail', lookup_field='slug')
    class Meta:
        model = Diary
        fields =[
            'timestamp',
            'url',

]


class DiaryDetailSerailizer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Diary
        fields = [
            'title',
            'timestamp',
            'content',
            'slug',
            'user'
        ]
    def get_user(self,obj):
        return str(obj.user.username)
class DiaryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = [
            'title',
            'content',
        ]
