from typing import ClassVar

from django.utils.translation import gettext_lazy as _

from django.db import models
from rest_framework.fields import DateTimeField


class Table(models.Model):
    """
    Model representing a table in restaurant.
    """
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at')
    )

    class Meta:
        verbose_name = _('Table')
        verbose_name_plural = _('Tables')
