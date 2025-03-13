from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from menu.views import ProvisionViewSet, MenuViewSet
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
router = routers.DefaultRouter()
router.register(r"provision", ProvisionViewSet)
router.register(r"menu", MenuViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
