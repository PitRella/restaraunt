from typing import ClassVar

from django.utils.translation import gettext_lazy as _

from django.db import models
from django.db.models import OneToOneField
from rest_framework.fields import DateTimeField


class Reserve(models.Model):
    """
    Model representing a reserving table in restaurant.
    """
    user = models.OneToOneField(
        "user.CustomUser",
        on_delete=models.CASCADE,
        verbose_name=_('Who created reservation')
    )
    table = models.OneToOneField(
        "tables.Table",
        on_delete=models.CASCADE,
        verbose_name=_('Бронь столика')
    )
    reserved_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_(
            'Reserved at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at')
    )

    class Meta:
        verbose_name = _('Reservation')
        verbose_name_plural = _('Reservations')
