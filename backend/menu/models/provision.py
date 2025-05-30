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

from menu.utils import provision_image_path


class Provision(models.Model):
    name: ClassVar[CharField] = models.CharField(
        max_length=100,
        verbose_name=_("Provision name")
    )
    slug: ClassVar[SlugField] = models.SlugField(
        unique=True
    )
    image: ClassVar[models.ImageField] = models.ImageField(
        upload_to=provision_image_path,
        verbose_name=_("Image")
    )
    description: ClassVar[TextField] = models.TextField(
        max_length=500,
        verbose_name=_("Description")
    )
    price: ClassVar[DecimalField] = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Price")
    )
    calories: ClassVar[
        PositiveSmallIntegerField] = models.PositiveSmallIntegerField(
        verbose_name=_("Calories")
    )
    grams: ClassVar[
        PositiveSmallIntegerField] = models.PositiveSmallIntegerField(
        verbose_name=_("Weight")
    )
    menus: ClassVar[ManyToManyField] = models.ManyToManyField(
        "ProvisionMenu",
        related_name="dishes",
        verbose_name=_("Dishes menu's")
    )

    def __str__(self):
        return f"{self.name or "No name dish"}"
