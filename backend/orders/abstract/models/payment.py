from django.db import models
from typing import ClassVar
from django.utils.translation import gettext_lazy as _

from django.db.models import (
    ForeignKey,
    ManyToManyField, PositiveSmallIntegerField,
    CharField,
    BooleanField,
    TextField,
    DateTimeField, OneToOneField, DecimalField
)
from base.models import TimeStamp


class AbstractPayment(models.Model, TimeStamp):
    """Abstract payment model"""
    order: ClassVar[OneToOneField] = models.OneToOneField(
        "orders.orders",
        on_delete=models.CASCADE,
        related_name="%(class)s_payment",
        verbose_name=_("Order")
    )
    amount: ClassVar[DecimalField] = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Amount")
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} - {self.amount}₴"
