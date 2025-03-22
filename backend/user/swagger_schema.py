from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from user.serializers import UserOutSerializer

user_documentation = extend_schema_view(
    list=extend_schema(
        summary='Список всіх користувачів. Доступно тільки адміністратору',
        description="Отримати список всіх користувачів які є в системі.",
        responses={
            HTTP_200_OK: UserOutSerializer,
        }
    ),
    update=extend_schema(
        summary='Оновити інформацію про користувача. Доступно для користувача та адміна.',
        description="Оновити користувача по його ID.",
        responses={
            HTTP_200_OK: UserOutSerializer,
            HTTP_404_NOT_FOUND: OpenApiResponse(
                response=None,
                description='Користувача за ID не знайдено'),
        }
    ),
    create=extend_schema(
        summary="Створити користувача. Не вимагає аутентифікації",
        description="Створення користувача, не вимагає жодної аутентифікації.",

        responses={
            HTTP_201_CREATED: UserOutSerializer,
        }
    ),
    retrieve=extend_schema(
        summary="Отримати користувача по ID. Доступно для користувача та адміна.",
        description="Отримати інформацію про конкретного користувача може лише адмін або сам користувач.",

        responses={
            HTTP_201_CREATED: UserOutSerializer,
        }
    ),
    destroy=extend_schema(
        summary="Видалити користувача по ID. Доступно для користувача та адміна.",
        description="Видалити конкретного користувача може лише адмін або сам користувач.",
        responses={
            HTTP_204_NO_CONTENT: OpenApiResponse()
        }
    )

)
