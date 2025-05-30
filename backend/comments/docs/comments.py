from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiResponse)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND
)

from comments.serializers import CommentSerializer, CommentCreateSerializer

comments_documentation = extend_schema_view(
    list=extend_schema(
        summary='List of all comments',
        responses={
            HTTP_200_OK: CommentSerializer,
        }
    ),
    update=extend_schema(
        summary='Update comment by ID',
        responses={
            HTTP_200_OK: CommentSerializer,
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Comment by ID not found'),
        }
    ),
    create=extend_schema(
        summary="Create comment.",
        responses={
            HTTP_201_CREATED: CommentCreateSerializer,
        }
    ),
    retrieve=extend_schema(
        summary="Get comment by ID",
        responses={
            HTTP_201_CREATED: CommentSerializer,
        }
    ),
    destroy=extend_schema(
        summary="Delete comment by ID.",
        responses={
            HTTP_204_NO_CONTENT: OpenApiResponse()
        }
    )

)
