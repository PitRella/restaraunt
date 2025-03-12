from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from menu.views import DishViewSet, MenuViewSet

router = routers.DefaultRouter()
router.register(r"dish", DishViewSet)
router.register(r"menu", MenuViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
