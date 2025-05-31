import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from menu.models import Provision


def provision_image_path(instance: "Provision", filename: str) -> str:
    """
    Create path for dish images.
    :param instance:
    :param filename:
    :return:
    """
    return os.path.join(f'images/dishes/{instance.slug}', filename)
