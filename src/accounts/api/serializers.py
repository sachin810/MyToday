from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class AccountCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]
    def validate_email(self,value):
        data = self.get_initial()
        email = data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise serializers.ValidationError('This Email has already taken')
        return value

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class AccountLoginSerializer(serializers.Serializer):

    token = serializers.CharField(read_only=True,allow_blank=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if not username:
            raise serializers.ValidationError('You must enter a valid username')
        user = User.objects.filter(
            Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError('Username does not exists')
        if not user_obj.check_password(password):
            raise serializers.ValidationError('Incorrect Password')
        data['token'] = 'SOME RANDOM TOKEN'
        return data
