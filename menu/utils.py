import os

def dish_image_path(instance: "Dish", filename: str) -> str:
    """
    Create path for dish images.
    :param instance:
    :param filename:
    :return:
    """
    return os.path.join(f'images/dishes/{instance.slug}', filename)