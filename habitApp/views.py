from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habitApp.serializers import HabitSerializer


class CreateHabitAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]
        return (permission() for permission in permissions)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)
