from django.contrib import admin
from menu.models import DishMenu, Dish


@admin.register(DishMenu)
class DishMenuAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    raw_id_fields = ['menus',]
    prepopulated_fields = {"slug": ("name",)}
