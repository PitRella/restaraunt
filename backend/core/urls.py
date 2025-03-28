from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from comments.views import CommentsViewSet
from menu.views import ProvisionViewSet, MenuViewSet
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from user.views import UserViewSet, CustomTokenObtainPairView
router = routers.DefaultRouter()
router.register(r"provision", ProvisionViewSet)
router.register(r"menu", MenuViewSet)
router.register(r"user", UserViewSet)
router.register(r"comment", CommentsViewSet)

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # api
    path("api/", include(router.urls)),
    # jwt
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
