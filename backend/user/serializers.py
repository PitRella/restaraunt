from rest_framework.serializers import ModelSerializer

from user.models import CustomUser


class UserOutSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'avatar')
        read_only_fields = ('email',)
