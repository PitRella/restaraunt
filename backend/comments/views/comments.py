from rest_framework.viewsets import ModelViewSet

from comments.models import Comment
from comments.serializers import CommentSerializer
from comments.docs.comments import comments_documentation


@comments_documentation
class CommentsViewSet(ModelViewSet):
    """
    ViewSet for  comments.
    """
    queryset = Comment.objects.all()
    http_method_names = ["get", "post", "put", "delete"]

    def get_serializer_class(self):
        """
        Return appropriate serializer class.
        :return:
        """
        match self.action:
            case "list":
                return CommentSerializer
            case "create":
                return CommentSerializer
        return CommentSerializer
