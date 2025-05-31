from typing import Type, Union, cast, List
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    BasePermission,
    AllowAny,
    IsAdminUser,
    IsAuthenticated
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from user.models import CustomUser
from user.schema import JwtTokenPair
from user.serializers.user import (
    CustomTokenObtainPairSerializer,
    UserRegisterSerializer,
    UserOutSerializer,
)
from user.docs.user import user_documentation


@user_documentation
class UserViewSet(ModelViewSet):
    """View set for handling user-related actions"""
    queryset = CustomUser.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_permissions(self) -> List[BasePermission]:
        match self.action:
            case "create":
                return [AllowAny()]
            case "list":
                return [IsAdminUser()]
            case "update" | "delete" | "retrieve":
                return [IsAdminUser(), IsAuthenticated()]
            case "registration":
                return [AllowAny()]
        return cast(List[BasePermission], super().get_permissions())

    def get_serializer_class(self) -> Type[
        Union
        [
            UserOutSerializer,
            UserRegisterSerializer
        ]
    ]:
        match self.action:
            case "registration":
                return UserRegisterSerializer
        return UserOutSerializer

    @action(detail=False, methods=["post"])
    def registration(self, request: Request) -> Response:
        serializer = cast(
            UserRegisterSerializer,
            self.get_serializer(
                data=request.data
            )
        )
        serializer.is_valid(raise_exception=True)
        user: CustomUser = serializer.save()
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response(
            data=JwtTokenPair(
                refresh=str(refresh),
                access=str(access)
            ).to_dict(),
            status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    """View to obtain access and refresh tokens."""
    serializer_class = CustomTokenObtainPairSerializer
