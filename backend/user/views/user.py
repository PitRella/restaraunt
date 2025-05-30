from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers.user import CustomTokenObtainPairSerializer, UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import CustomUser
from user.serializers.user import UserOutSerializer
from user.docs.user import user_documentation

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


@user_documentation
class UserViewSet(ModelViewSet):
    """
    View set for handle actions with users
    """
    queryset = CustomUser.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_permissions(self):
        match self.action:
            case "create":
                return [AllowAny()]
            case 'list':
                return [IsAdminUser()]
            case "update" | "delete" | "retrieve":
                return [IsAdminUser(), IsAuthenticated()]
            case "registration":
                return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        """
        Return appropriate serializer class.
        :return:
        """
        match self.action:
            case "registration":
                return UserRegisterSerializer
        return UserOutSerializer

    @action(detail=False, methods=['post'])
    def registration(self, request, pk=None):
        serializer: "UserRegisterSerializer" = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user: "CustomUser" = serializer.save()
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        return Response({
            'refresh': str(refresh),
            'access': str(access),
        }, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    """Class View to get access token."""
    serializer_class = CustomTokenObtainPairSerializer
