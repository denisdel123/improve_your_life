from django.urls import path

from habitApp.apps import HabitappConfig
from habitApp.views import CreateHabitAPIView, ListOwnerHabitAPIView, ListPublicHabitAPIView, UpdateHabitAPIView, \
    DestroyHabitAPIView

app_name = HabitappConfig.name
urlpatterns = [

    path('create/', CreateHabitAPIView.as_view(), name='create-habit'),
    path('list/', ListOwnerHabitAPIView.as_view(), name='list-habit'),
    path('list/public/', ListPublicHabitAPIView.as_view(), name='list-public-habit'),
    path('update/<int:pk>/', UpdateHabitAPIView.as_view(), name='update-habit'),
    path('destroy/<int:pk>/', DestroyHabitAPIView.as_view(), name='destroy-habit')
]