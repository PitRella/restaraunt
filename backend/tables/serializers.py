from rest_framework.serializers import ModelSerializer

from tables.models import Table, Reserve


class BaseReserveSerializer(ModelSerializer):
    """Base serializer for a table reserve"""

    class Meta:
        model = Reserve
        fields = '__all__'


class TableOutSerializer(ModelSerializer):
    """
    Serializer for a table out including reserve
    """
    reserve = BaseReserveSerializer(read_only=True)

    class Meta:
        model = Table
        fields = '__all__'
