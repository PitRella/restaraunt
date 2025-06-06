
from django.utils.translation import gettext_lazy as _

from django.db import models

from orders.abstract.models import AbstractPayment


class TerminalPayment(AbstractPayment):
    """Payment using terminal"""
    terminal_id = models.CharField(
        max_length=50,
        verbose_name=_("Terminal ID"),
    )

    class Meta:
        verbose_name = _("Terminal payment")
        verbose_name_plural = _("Terminal payments")
