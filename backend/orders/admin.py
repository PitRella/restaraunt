from django.contrib import admin

from orders.models import Order, CashPayment, CardPayment, TerminalPayment


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "delivery_type", "created_at")


@admin.register(CashPayment)
class CashPaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "date_time")


@admin.register(CardPayment)
class CardPaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "date_time")


@admin.register(TerminalPayment)
class TerminalPaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "date_time")
