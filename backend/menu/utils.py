import os

def provision_image_path(instance: "Provision", filename: str) -> str:
    """
    Create path for dish images.
    :param instance:
    :param filename:
    :return:
    """
    return os.path.join(f'images/dishes/{instance.slug}', filename)