from rest_framework.serializers import ModelSerializer

from tables.models import Table
from tables.serializers.reserve import ReserveSerializer


class TableSerializer(ModelSerializer):
    """Serializer for a table out including reserve"""
    reserve = ReserveSerializer(read_only=True)

    class Meta:
        model = Table
        fields = '__all__'
