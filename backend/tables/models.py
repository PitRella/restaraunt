from django.db import models
from django.utils.translation import gettext_lazy as _


class Table(models.Model):
    """
    Model representing a table in restaurant.
    """
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Час оновлення'))


class Reserve(models.Model):
    """
    Model representing a reserving table in restaurant.
    """
    user = models.OneToOneField("user.CustomUser", on_delete=models.CASCADE, verbose_name=_('Хто зробив бронь'))
    table = models.OneToOneField("tables.Table", on_delete=models.CASCADE, verbose_name=_('Бронь столика'))
    reserved_at = models.DateTimeField(auto_now=True, verbose_name=_('Час на коли зарезервовано'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Час останнього оновлення'))
