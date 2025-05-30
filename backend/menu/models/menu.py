from typing import ClassVar

from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _

from base.models import TimeStamp


class ProvisionMenu(models.Model, TimeStamp):
    name: ClassVar[CharField] = models.CharField(
        max_length=255,
        verbose_name=_('Menu')
    )

    def __str__(self):
        return f"{self.name or "Menu without name"}"
