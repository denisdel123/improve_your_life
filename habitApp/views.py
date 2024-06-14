from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from UserApp.permissions import IsOwner
from habitApp.models import Habit
from habitApp.paginations import CustomPagination
from habitApp.permissions import IsOwnerHabit
from habitApp.serializers import HabitSerializer


class CreateHabitAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]
        return (permission() for permission in permissions)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)


class ListOwnerHabitAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        habit = Habit.objects.filter(owner=self.request.user)
        return habit


class ListPublicHabitAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        habit = Habit.objects.filter(is_public=True)
        return habit


class UpdateHabitAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, IsAdminUser | IsOwnerHabit]
        return super().get_permissions()


class DestroyHabitAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, IsAdminUser | IsOwnerHabit]
        return super().get_permissions()
