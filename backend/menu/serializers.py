from rest_framework.serializers import ModelSerializer

from menu.models import Provision, ProvisionMenu


class ProvisionOutSerializer(ModelSerializer):
    """
    Base serializer for dish models, returns the most important fields.
    """
    class Meta:
        model = Provision
        fields = [
            'name',
            'grams',
            'calories',
            'price',
            'image',
        ]

class MenuSerializer(ModelSerializer):
    class Meta:
        model = ProvisionMenu
        fields = "__all__"