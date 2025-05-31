from typing import Type, Union

from menu.docs import provision_documentation
from rest_framework.viewsets import ModelViewSet

from menu.models import Provision
from menu.serializers import ProvisionOutSerializer, ProvisionCreateSerializer


@provision_documentation
class ProvisionViewSet(ModelViewSet):
    """
    ViewSet for dishes.
    """
    queryset = Provision.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_serializer_class(self) -> Type[
        Union[
            ProvisionOutSerializer,
            ProvisionCreateSerializer
        ]
    ]:
        """Return the appropriate serializer class."""
        match self.action:
            case "list":
                return ProvisionOutSerializer
            case "create":
                return ProvisionCreateSerializer
        return ProvisionOutSerializer
