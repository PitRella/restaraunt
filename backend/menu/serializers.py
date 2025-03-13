from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

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


class ProvisionCreateSerializer(ModelSerializer):
    """
    Serializer for creating a dish with menu selection.
    """
    menus = PrimaryKeyRelatedField(
        queryset=ProvisionMenu.objects.all(),
        many=True
    )

    class Meta:
        model = Provision
        fields = [
            'name',
            'slug',
            'image',
            'description',
            'price',
            'calories',
            'grams',
            'menus'
        ]


class MenuSerializer(ModelSerializer):
    class Meta:
        model = ProvisionMenu
        fields = "__all__"
