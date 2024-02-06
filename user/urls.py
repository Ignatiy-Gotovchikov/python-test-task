from django.urls import path, include
from rest_framework.routers import SimpleRouter

from user.views.user import UserViewSet

user_router = SimpleRouter()
user_router.register(
    prefix="user", viewset=UserViewSet, basename="User"
)

urlpatterns = [
    path('', include(user_router.urls)),
]
