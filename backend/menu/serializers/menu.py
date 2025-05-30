from rest_framework.serializers import ModelSerializer

from menu.models import ProvisionMenu

class MenuSerializer(ModelSerializer):
    class Meta:
        model = ProvisionMenu
        fields = "__all__"