from django.contrib import admin
from tables.models import Reserve


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    pass
