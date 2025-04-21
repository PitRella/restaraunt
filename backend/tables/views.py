from rest_framework.viewsets import ModelViewSet

from tables.models import Table, Reserve
from tables.serializers import TableOutSerializer


class TableViewSet(ModelViewSet):
    """
    ViewSet for dishes.
    """
    queryset = Table.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_serializer_class(self):
        """
        Return appropriate serializer class.
        :return:
        """
        return TableOutSerializer
