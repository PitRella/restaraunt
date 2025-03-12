from rest_framework.viewsets import ModelViewSet

from menu.models import Dish, DishMenu
from menu.serializers import DishOutSerializer, MenuSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
class DishViewSet(ModelViewSet):
    """
    ViewSet for dishes.
    """
    queryset = Dish.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "list":
                return DishOutSerializer
        return super().get_serializer_class()

class MenuViewSet(ModelViewSet):
    queryset = DishMenu.objects.all()
    serializer_class = MenuSerializer
