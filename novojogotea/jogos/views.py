from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import MemoryGame
from .serializers import UserSerializer, MemoryGameSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MemoryGameViewSet(viewsets.ModelViewSet):
    queryset = MemoryGame.objects.all()
    serializer_class = MemoryGameSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
