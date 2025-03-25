from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from .serializers import CommentSerializer, CommentCreateSerializer

comments_documentation = extend_schema_view(
    list=extend_schema(
        summary='Список всіх коментарів',
        responses={
            HTTP_200_OK: CommentSerializer,
        }
    ),
    update=extend_schema(
        summary='Оновити коментар',
        responses={
            HTTP_200_OK: CommentSerializer,
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Коментар за ID не знайдено'),
        }
    ),
    create=extend_schema(
        summary="Створити коментар",
        responses={
            HTTP_201_CREATED: CommentCreateSerializer,
        }
    ),
    retrieve=extend_schema(
        summary="Отримати коментар по ID",
        responses={
            HTTP_201_CREATED: CommentSerializer,
        }
    ),
    destroy=extend_schema(
        summary="Видалити коментар по  ID",
        responses={
            HTTP_204_NO_CONTENT: OpenApiResponse()
        }
    )

)
