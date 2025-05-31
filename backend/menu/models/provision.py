from typing import ClassVar
from django.db.models.fields import (
    CharField,
    SlugField,
    TextField,
    DecimalField,
    PositiveSmallIntegerField
)
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import gettext_lazy as _
from django.db import models

from base.models import TimeStamp
from menu.utils import provision_image_path


class Provision(TimeStamp):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Provision name")
    )
    slug = models.SlugField(
        unique=True
    )
    image = models.ImageField(
        upload_to=provision_image_path,
        verbose_name=_("Image")
    )
    description = models.TextField(
        max_length=500,
        verbose_name=_("Description")
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Price")
    )
    calories = models.PositiveSmallIntegerField(
        verbose_name=_("Calories")
    )
    grams = models.PositiveSmallIntegerField(
        verbose_name=_("Weight")
    )
    menus = models.ManyToManyField(
        "ProvisionMenu",
        related_name="dishes",
        verbose_name=_("Dishes menu's")
    )

    def __str__(self):
        return f"{self.name or "No name dish"}"
