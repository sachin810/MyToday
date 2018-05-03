from .serializers import DiaryListSerailizer,DiaryDetailSerailizer,DiaryCreateSerializer
from rest_framework import views
from rest_framework import generics
from diary.models import Diary
from .permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated



class DiaryListApiView(generics.ListAPIView):
    def get_queryset(self):
        """
        Filter objects so a user only sees his own stuff.
        If user is admin, let him see all.
        """
        if self.request.user.is_staff:
            return Diary.objects.all()
        else:
            return Diary.objects.filter(user=self.request.user)

    serializer_class = DiaryListSerailizer
    permission_classes = [IsAuthenticated,IsOwnerOrAdmin]

class DiaryDetailApiView(generics.RetrieveAPIView):
    def get_queryset(self):
        if self.request.user.is_staff:
            return Diary.objects.all()
        else:
            return Diary.objects.filter(user = self.request.user)
    serializer_class = DiaryDetailSerailizer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

class DiaryCreateApiView(generics.CreateAPIView):
    def get_queryset(self):
        if self.request.user.is_staff:
            return Diary.objects.all()
        else:
            return Diary.objects.filter(user = self.request.user)
    serializer_class = DiaryCreateSerializer
    permission_classes = [IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class DiaryUpdateApiView(generics.RetrieveUpdateAPIView):
    def get_queryset(self):
        if self.request.user.is_staff:
            return Diary.objects.all()
        else:
            return Diary.objects.filter(user = self.request.user)
    serializer_class = DiaryCreateSerializer
    permission_classes = [IsOwnerOrAdmin]
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(user = self.request.user)

class DeleteDiaryApiView(generics.DestroyAPIView):
    def get_queryset(self):
        if self.request.user.is_staff:
            return Diary.objects.all()
        else:
            return Diary.objects.filter(user = self.request.user)
    serializer_class = DiaryCreateSerializer
    permission_classes = [IsOwnerOrAdmin]
    lookup_field = 'slug'