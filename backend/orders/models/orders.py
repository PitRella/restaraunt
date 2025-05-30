from typing import ClassVar

from django.utils.translation import gettext_lazy as _

from django.db import models
import enum
from django.db.models import (
    ForeignKey,
    ManyToManyField, PositiveSmallIntegerField,
    CharField,
    BooleanField,
    TextField,
    DateTimeField
)

from base.models import TimeStamp


class DeliveryType(enum.Enum):
    """Delivery types for order"""

    DELIVERY = 0
    PICKUP = 1

    @classmethod
    def choices(cls) -> list[tuple[int, str]]:
        return [(key.value, key.name) for key in cls]


class Order(models.Model, TimeStamp):
    # Main fields
    customer: ClassVar[ForeignKey] = models.ForeignKey(
        "user.CustomUser",
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("Customer")
    )
    products: ClassVar[ManyToManyField] = models.ManyToManyField(
        "menu.Provision",
        related_name="order_products",
        verbose_name=_("Products")
    )
    delivery_type: ClassVar[
        PositiveSmallIntegerField] = models.PositiveSmallIntegerField(
        choices=DeliveryType.choices(),
        verbose_name=_("Delivery type"),
    )
    # Order details
    address: ClassVar[CharField] = models.CharField(
        verbose_name=_("Delivery address"),
        max_length=255,
        null=True, blank=True,
    )
    comment: ClassVar[TextField] = models.TextField(
        verbose_name=_("Comment to order"),
        null=True, blank=True
    )
    is_quickly: ClassVar[BooleanField] = models.BooleanField(
        verbose_name=_("As soon as possible?"),
        null=True, blank=True,
        default=False
    )
    tableware_amount: ClassVar[
        PositiveSmallIntegerField] = models.PositiveSmallIntegerField(
        verbose_name=_("Tableware amount")
    )
    desired_time: ClassVar[DateTimeField] = models.DateTimeField(
        verbose_name=_("Час отримання замовлення"),
        null=True, blank=True,
        default=None
    )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


