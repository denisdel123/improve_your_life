from django.urls import path

from habitApp.apps import HabitappConfig
from habitApp.views import CreateHabitAPIView, ListOwnerHabitAPIView, ListPublicHabitAPIView, UpdateHabitAPIView, \
    DestroyHabitAPIView

app_name = HabitappConfig.name
urlpatterns = [

    path('create/', CreateHabitAPIView.as_view(), name='habit-create'),
    path('list/', ListOwnerHabitAPIView.as_view(), name='habit-list'),
    path('list/public/', ListPublicHabitAPIView.as_view(), name='habit-list-public'),
    path('update/<int:pk>/', UpdateHabitAPIView.as_view(), name='habit-update'),
    path('destroy/<int:pk>/', DestroyHabitAPIView.as_view(), name='habit-destroy')
]