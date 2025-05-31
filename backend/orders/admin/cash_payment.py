from django.contrib import admin

from orders.models import CashPayment


@admin.register(CashPayment)
class CashPaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "created_at")
