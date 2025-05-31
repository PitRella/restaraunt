from django.contrib import admin
from menu.models import ProvisionMenu


@admin.register(ProvisionMenu)
class ProvisionMenuAdmin(admin.ModelAdmin):
    list_display = ("name",)

