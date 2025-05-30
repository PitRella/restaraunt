from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiResponse
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND
)

from menu.serializers import (
    MenuSerializer,
    ProvisionOutSerializer,
)

menu_documentation = extend_schema_view(
    list=extend_schema(
        summary="Get all menus.",
        responses={
            HTTP_200_OK: MenuSerializer,
        }
    ),
    update=extend_schema(
        summary="Change menus",
        responses={
            HTTP_200_OK: MenuSerializer,
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Menu by ID not found.'),
        }
    ),
    create=extend_schema(
        summary="Create menu",
        responses={
            HTTP_201_CREATED: MenuSerializer,
        }
    ),
    destroy=extend_schema(
        summary="Delete menu by ID.",
        responses={
            HTTP_200_OK: OpenApiResponse(
                response=None,
                description='Menu success deleted'),
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Menu by ID not found.'),
        }
    ),
    retrieve=extend_schema(
        summary="Get all menu by ID.",
        responses={
            HTTP_204_NO_CONTENT: MenuSerializer,
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Menu by ID not found.'),
        }
    ),
    dishes=extend_schema(
        summary="Get all provisions by menu ID.",
        responses={
            HTTP_200_OK: OpenApiResponse(
                response=ProvisionOutSerializer(many=True),
                description='List of all provisions in menu'
            ),
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Menu by ID not found.'),
        }
    )
)
