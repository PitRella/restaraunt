from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

from comments.views import CommentsViewSet
from menu.views import ProvisionViewSet, MenuViewSet
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from orders.views import OrderViewSet
from tables.views import TableViewSet
from user.views import UserViewSet, CustomTokenObtainPairView

router = routers.DefaultRouter()
router.register(r"provision", ProvisionViewSet)
router.register(r"menu", MenuViewSet)
router.register(r"user", UserViewSet)
router.register(r"comment", CommentsViewSet)
router.register(r"table", TableViewSet)
router.register(r"order", OrderViewSet)

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # api
    path("api/", include(router.urls)),
    # jwt
    path('api/token/',
         CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'
         ),
    path('api/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'
         ),
    # swagger
    path('api/schema/',
         SpectacularAPIView.as_view(),
         name='schema'),
    path('api/docs/',
         SpectacularSwaggerView.as_view(
             url_name='schema'
         ),
         name='docs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
