from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStamp(models.Model):
    """Abstract model class that provides self-managed timestamp fields.

    This model can be inherited by other models to automatically include
    timestamp tracking fields.

    Fields:
        created_at: Timestamp when the object was created, set automatically
        updated_at: Timestamp of the last update, updated automatically
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at")
    )

    class Meta:
        abstract = True
