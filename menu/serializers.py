from rest_framework.serializers import ModelSerializer

from menu.models import Dish, DishMenu


class DishOutSerializer(ModelSerializer):
    """
    Base serializer for dish models, returns the most important fields.
    """
    class Meta:
        model = Dish
        fields = [
            'name',
            'grams',
            'calories',
            'price',
            'image',
        ]

class MenuSerializer(ModelSerializer):
    class Meta:
        model = DishMenu
        fields = "__all__"