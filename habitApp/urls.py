from django.urls import path

from habitApp.apps import HabitappConfig
from habitApp.views import CreateHabitAPIView

app_name = HabitappConfig.name
urlpatterns = [
    path('create/', CreateHabitAPIView.as_view(), name='create-habit'),
]