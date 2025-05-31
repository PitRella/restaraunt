
from django.utils.translation import gettext_lazy as _

from django.db import models
import enum
from base.models import TimeStamp


class DeliveryType(enum.Enum):
    """Delivery types for order"""

    DELIVERY = 0
    PICKUP = 1

    @classmethod
    def choices(cls) -> list[tuple[int, str]]:
        return [(key.value, key.name) for key in cls]


class Order(TimeStamp):
    # Main fields
    customer = models.ForeignKey(
        "user.CustomUser",
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("Customer")
    )
    products = models.ManyToManyField(
        "menu.Provision",
        related_name="order_products",
        verbose_name=_("Products")
    )
    delivery_type = models.PositiveSmallIntegerField(
        choices=DeliveryType.choices(),
        verbose_name=_("Delivery type"),
    )
    # Order details
    address = models.CharField(
        verbose_name=_("Delivery address"),
        max_length=255,
        null=True, blank=True,
    )
    comment = models.TextField(
        verbose_name=_("Comment to order"),
        null=True, blank=True
    )
    is_quickly  = models.BooleanField(
        verbose_name=_("As soon as possible?"),
        null=True, blank=True,
        default=False
    )
    tableware_amount = models.PositiveSmallIntegerField(
        verbose_name=_("Tableware amount")
    )
    desired_time = models.DateTimeField(
        verbose_name=_("Час отримання замовлення"),
        null=True, blank=True,
        default=None
    )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
