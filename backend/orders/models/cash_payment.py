from typing import ClassVar

from django.utils.translation import gettext_lazy as _

from django.db import models
from django.db.models import DecimalField

from orders.abstract.models import AbstractPayment


class CashPayment(AbstractPayment):
    """Payment using cash"""
    cash_given = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Купюра")
    )

    class Meta:
        verbose_name = _("Cash payment")
        verbose_name_plural = _("Cash payments")
