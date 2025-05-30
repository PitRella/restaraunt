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
    ProvisionOutSerializer,
    ProvisionCreateSerializer
)

provision_documentation = extend_schema_view(
    list=extend_schema(
        summary='List of all provisions(include drinks and dishes)',
        responses={
            HTTP_200_OK: ProvisionOutSerializer,
        }
    ),
    update=extend_schema(
        summary='Оновити продукт',
        responses={
            HTTP_200_OK: ProvisionOutSerializer,
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Provision by ID not found.'),
        }
    ),
    create=extend_schema(
        summary="Create provision.",
        responses={
            HTTP_201_CREATED: ProvisionCreateSerializer,
        }
    ),
    retrieve=extend_schema(
        summary="Get provision by ID. Drinks and dishes are included.",
        responses={
            HTTP_201_CREATED: ProvisionOutSerializer,
        }
    ),
    destroy=extend_schema(
        summary="Delete provision by ID.",
        responses={
            HTTP_204_NO_CONTENT: OpenApiResponse()
        }
    )

)
