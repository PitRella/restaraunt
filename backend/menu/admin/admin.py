from django.contrib import admin
from menu.models import ProvisionMenu, Provision


@admin.register(ProvisionMenu)
class ProvisionMenuAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Provision)
class ProvisionAdmin(admin.ModelAdmin):
    raw_id_fields = ['menus', ]
    prepopulated_fields = {"slug": ("name",)}
