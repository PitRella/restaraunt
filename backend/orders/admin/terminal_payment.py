from django.contrib import admin

from orders.models import TerminalPayment



@admin.register(TerminalPayment)
class TerminalPaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "created_at")
