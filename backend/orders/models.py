from django.utils.translation import gettext_lazy as _

from django.db import models
import enum


class DeliveryType(enum.Enum):
    """Delivery types for order"""

    DELIVERY = 0
    PICKUP = 1

    @classmethod
    def choices(cls) -> list[tuple[int, str]]:
        return [(key.value, key.name) for key in cls]


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
    delivery_type = models.PositiveSmallIntegerField(choices=DeliveryType.choices())
    # Order details
    address = models.CharField(
        verbose_name=_("Адреса доставки"),
        max_length=255,
        null=True, blank=True,
    )
    comment = models.TextField(
        verbose_name=_("Коментар до замовлення"),
        null=True, blank=True
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


class AbstractPayment(models.Model):
    """Abstract payment model"""
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="%(class)s_payment",
        verbose_name=_("Замовлення")
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Сума"))
    date_time = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата та час платежу"))

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} - {self.amount}₴"


class CashPayment(AbstractPayment):
    """Payment using cash"""
    cash_given = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Купюра")
    )

    class Meta:
        verbose_name = _("Оплата готівкою")
        verbose_name_plural = _("Оплати готівкою")


class CardPayment(AbstractPayment):
    """Payment using card online"""
    card_last_digits = models.CharField(
        max_length=4,
        verbose_name=_("Останні 4 цифри картки"),
        null=True, blank=True
    )

    class Meta:
        verbose_name = _("Оплата карткою")
        verbose_name_plural = _("Оплати картками")


class TerminalPayment(AbstractPayment):
    """Payment using terminal"""
    terminal_id = models.CharField(
        max_length=50,
        verbose_name=_("ID терміналу"),
        null=True, blank=True
    )

    class Meta:
        verbose_name = _("Оплата через термінал")
        verbose_name_plural = _("Оплати через термінали")
