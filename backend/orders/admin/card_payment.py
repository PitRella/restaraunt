from django.contrib import admin

from orders.models import CardPayment


@admin.register(CardPayment)
class CardPaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "created_at")