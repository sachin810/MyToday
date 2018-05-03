from .serializers import AccountCreateSerializer,AccountLoginSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import views
from rest_framework import permissions
from rest_framework import response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
User = get_user_model()

class AccountCreateApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountCreateSerializer

class AccountLoginApiView(views.APIView):
    serializer_class = AccountLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = AccountLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return response.Response(new_data,HTTP_200_OK)
        return response.Response(serializer.errors,HTTP_400_BAD_REQUEST)
