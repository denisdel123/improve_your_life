from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from habitApp.models import Habit
from habitApp.paginations import CustomPagination
from habitApp.permissions import IsOwnerHabit
from habitApp.serializers import HabitSerializer

"""Эндпоинт для создания привычки."""


class CreateHabitAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)


"""Эндпоинт для вывода всех привычек пользователя."""


class ListOwnerHabitAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        habit = Habit.objects.filter(owner=self.request.user)
        return habit


"""Эндпоинт для вывода публичных привычек."""


class ListPublicHabitAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        habit = Habit.objects.filter(is_public=True)
        return habit


"""Эндпоинт для изменения привычки."""


class UpdateHabitAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwnerHabit]


"""Эндпоинт для удаления привычки."""


class DestroyHabitAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwnerHabit]
