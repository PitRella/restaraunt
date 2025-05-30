
from django.utils.translation import gettext_lazy as _

from django.db import models

from orders.abstract.models import AbstractPayment


class CardPayment(AbstractPayment):
    """Payment using card online"""
    card_last_digits = models.CharField(
        max_length=4,
        verbose_name=_("Card last 4 numbers"),
    )

    class Meta:
        verbose_name = _("Card payment")
        verbose_name_plural = _("Card payments")
