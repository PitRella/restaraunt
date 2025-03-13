from rest_framework.viewsets import ModelViewSet

from menu.models import Provision, ProvisionMenu
from menu.serializers import ProvisionOutSerializer, MenuSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from menu.swagger_schema import menu_documentation


class ProvisionViewSet(ModelViewSet):
    """
    ViewSet for dishes.
    """
    queryset = Provision.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    def get_serializer_class(self):
        """
        Return appropriate serializer class.
        :return:
        """
        match self.action:
            case "list":
                return ProvisionOutSerializer
        return super().get_serializer_class()


@menu_documentation
class MenuViewSet(ModelViewSet):
    queryset = ProvisionMenu.objects.all()
    serializer_class = MenuSerializer
    http_method_names = ["get", "post", "put", "delete"]

    @action(detail=True, methods=["get"])
    def dishes(self, request, pk=None):
        """Retrieve all dishes attached to menu"""
        menu = self.get_object()
        dishes = menu.dishes.all()
        serializer = ProvisionOutSerializer(dishes, many=True)
        return Response(serializer.data)
