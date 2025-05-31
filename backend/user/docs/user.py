from http.client import responses

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

from user.serializers.user import UserOutSerializer

user_documentation = extend_schema_view(
    list=extend_schema(
        summary='List of all users. Available only for administrator',
        description="Get a list of all users in the system.",
        responses={
            HTTP_200_OK: UserOutSerializer,
        }
    ),
    update=extend_schema(
        summary='Update user information.'
                ' Available for user and admin.',
        description="Update user by their ID.",
        responses={
            HTTP_200_OK: UserOutSerializer,
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='User with provided ID not found'),
        }
    ),
    create=extend_schema(
        summary="Create user. No authentication required",
        description="Create a user, no authentication required.",

        responses={
            HTTP_201_CREATED: UserOutSerializer,
        }
    ),
    retrieve=extend_schema(
        summary="Get user by ID. Available for"
                " user and admin.",
        description="Only admin or the user themselves can"
                    " get information about specific user.",

        responses={
            HTTP_201_CREATED: UserOutSerializer,
        }
    ),
    destroy=extend_schema(
        summary="Delete user by ID."
                " Available for user and admin.",
        description="Only admin or the user themselves can"
                    " delete specific user.",
        responses={
            HTTP_204_NO_CONTENT: OpenApiResponse()
        }
    ),
    registration=extend_schema(
        summary="Create user",
        description="Create user and get pair of tokens"),
    responses={
        HTTP_201_CREATED: UserOutSerializer,
    }
)
