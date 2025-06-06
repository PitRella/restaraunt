
from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import TimeStamp


class Comment(TimeStamp):
    author = models.ForeignKey(
        "user.CustomUser",
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_("Comment author")
    )
    text = models.TextField(
        max_length=500,
        verbose_name=_("Comment text")
    )
    is_approved = models.BooleanField(
        default=False,
        verbose_name=_("Is comment approved?"))

    def __str__(self):
        return f"{self.text[:50]}..."
