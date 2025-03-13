from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from menu.serializers import MenuSerializer, ProvisionOutSerializer

menu_documentation = extend_schema_view(
    list=extend_schema(
        summary="Отримати всі меню",
        responses={
            HTTP_200_OK: MenuSerializer,
        }
    ),
    update=extend_schema(
        summary="Зміна параметрів меню",
        responses={
            HTTP_200_OK: MenuSerializer,
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Меню за ID не знайдено'),
        }
    ),
    create=extend_schema(
        summary="Створити меню",
        responses={
            HTTP_201_CREATED: MenuSerializer,
        }
    ),
    destroy=extend_schema(
        summary="Видалити меню за ID",
        responses={
            HTTP_200_OK: OpenApiResponse(
                response=None,
                description='Меню успішно видалено'),
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Меню за ID не знайдено'),
        }
    ),
    retrieve=extend_schema(
        summary="Отримати меню за ID",
        responses={
            HTTP_204_NO_CONTENT: MenuSerializer,
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Меню за ID не знайдено'),
        }
    ),
    dishes=extend_schema(
        summary="Отримати всі страви меню",
        responses={
            HTTP_200_OK: OpenApiResponse(
                response=ProvisionOutSerializer(many=True),
                description='Список страв меню'
            ),
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Меню за ID не знайдено'),
        }
    )
)
