import os



def user_image_path(instance, filename: str) -> str:
    """
    Create path for user images.
    :param instance: User
    :param filename:
    :return:
    """
    return os.path.join(f'images/users/{instance.id}', filename)
