from rest_framework.serializers import ModelSerializer
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'text']
