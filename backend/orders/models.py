from django.utils.translation import gettext_lazy as _

from django.db import models


class Order(models.Model):
    # Main fields
    user = models.ForeignKey(
        "user.CustomUser",
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("Користувач")
    )
    products = models.ManyToManyField(
        "menu.Provision",
        related_name="order_products",
        verbose_name=_("Продукти")
    )
    # Order details
    address = models.CharField(
        verbose_name=_("Адреса доставки"),
    )
    comment = models.TextField(
        verbose_name=_("Коментар до замовлення",
                       null=True, blank=True
                       )
    )
    is_quickly = models.BooleanField(
        verbose_name=_("Якнайшвидше?"),
        null=True, blank=True,
        default=False
    )
    tableware_amount = models.PositiveSmallIntegerField(
        verbose_name=_("Кількість приладів")
    )
    has_specific_time = models.BooleanField(
        verbose_name=_("Доставка на конкретний час?"),
        null=True, blank=True,
        default=False
    )
    desired_time = models.TimeField(
        verbose_name=_("Час отримання замовлення"),
        null=True, blank=True,
        default=None
    )
    # Date fields
    created_at = models.DateTimeField(
        verbose_name=_("Дата створення"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Дата оновлення"),
        auto_now=True
    )
