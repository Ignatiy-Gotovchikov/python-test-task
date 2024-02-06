from rest_framework import viewsets
from user.models.user import User
from user.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        # Устанавливаем is_active в True перед созданием пользователя
        serializer.save(is_active=True)
