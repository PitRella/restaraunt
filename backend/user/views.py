from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from user.models import CustomUser
from user.serializers import UserOutSerializer
from user.swagger_schema import user_documentation
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

@user_documentation
class UserViewSet(ModelViewSet):
    """
    View set for handle actions with users
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserOutSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def get_permissions(self):
        match self.action:
            case "create":
                return [AllowAny()]
            case 'list':
                return [IsAdminUser()]
            case "update" | "delete" | "retrieve": 
                return [IsAdminUser(), IsAuthenticated()]
        return super().get_permissions()



class CustomTokenObtainPairView(TokenObtainPairView):
    """Class View to get access token."""
    serializer_class = CustomTokenObtainPairSerializer