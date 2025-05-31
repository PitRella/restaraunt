from django.contrib import admin
from menu.models import Provision


@admin.register(Provision)
class ProvisionAdmin(admin.ModelAdmin):
    raw_id_fields = ['menus', ]
    prepopulated_fields = {"slug": ("name",)}
