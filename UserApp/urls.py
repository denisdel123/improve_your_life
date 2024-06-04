from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from UserApp.apps import UserappConfig
from UserApp.views import Registration, UserListAPIView, UserRetrieveAPIView

app_name = UserappConfig.name

urlpatterns = [
    # user urls
    path('create/', Registration.as_view(), name='user-create'),
    path('list/', UserListAPIView.as_view(), name="user-list"),
    path('retrieve/<int:pk>/', UserRetrieveAPIView.as_view(), name="user-retrieve"),

    # urls token
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='access-token'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token-refresh'),
]