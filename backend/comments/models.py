from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    author = models.ForeignKey(
        "user.CustomUser",
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_("Автор")
    )
    text = models.TextField(
        max_length=500,
        verbose_name=_("Текст повідомлення")
    )
    is_approved = models.BooleanField(default=False, verbose_name=_("Коментар пройшов модерацію?"))
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата створення")
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Дата редагування")
    )

    def __str__(self):
        return f"{self.text[:50]}..."
