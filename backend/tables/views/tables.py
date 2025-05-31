from rest_framework.viewsets import ModelViewSet

from tables.models import Table
from tables.serializers import TableSerializer


class TableViewSet(ModelViewSet):
    """ViewSet for dishes."""
    queryset = Table.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_serializer_class(self) -> type[TableSerializer]:
        """
        Return the appropriate serializer class.
        :return:
        """
        return TableSerializer
