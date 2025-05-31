from rest_framework.serializers import ModelSerializer

from tables.models import Reserve


class ReserveSerializer(ModelSerializer):
    """Base serializer for a table reserve"""

    class Meta:
        model = Reserve
        fields = '__all__'
