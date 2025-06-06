from rest_framework.viewsets import ModelViewSet

from menu.models import ProvisionMenu
from menu.serializers import ProvisionOutSerializer, MenuSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from menu.services import MenuServiceImpl
from menu.docs import menu_documentation
from rest_framework.request import Request

from typing import Optional


@menu_documentation
class MenuViewSet(ModelViewSet):
    queryset = ProvisionMenu.objects.all()
    serializer_class = MenuSerializer
    http_method_names = ["get", "post", "put", "delete"]
    database_service = MenuServiceImpl

    @action(detail=True, methods=["get"])
    def dishes(self, request: Request, pk: Optional[str] = None) -> Response:
        """Retrieve all dishes attached to menu"""
        dishes = MenuServiceImpl.get_dishes_from_menu(self.get_object)
        serializer = ProvisionOutSerializer(dishes, many=True)
        return Response(serializer.data)
