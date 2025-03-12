from django.db import models
from django.utils.translation import gettext_lazy as _

from menu.utils import dish_image_path


class DishMenu(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Меню'))

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Назва страви"))
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=dish_image_path, verbose_name=_("Зображення страви"))
    description = models.TextField(max_length=500, verbose_name=_("Опис страви"))
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=_("Ціна"))
    calories = models.PositiveSmallIntegerField(verbose_name=_("Калорії"))
    grams = models.PositiveSmallIntegerField(verbose_name=_("Вага страви"))
    menus = models.ManyToManyField("DishMenu", related_name="dishes", verbose_name=_("Меню страви"))

    def __str__(self):
        return f"{self.name}"
