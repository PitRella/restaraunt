import os

def user_image_path(instance: "CustomUser", filename: str) -> str:
    """
    Create path for user images.
    :param instance:
    :param filename:
    :return:
    """
    return os.path.join(f'images/users/{instance.id}', filename)