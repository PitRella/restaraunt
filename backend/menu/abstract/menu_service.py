from abc import abstractmethod, ABC

from django.db.models import QuerySet

from menu.models import ProvisionMenu, Provision


class MenuService(ABC):

    @staticmethod
    @abstractmethod
    def get_dishes_from_menu(menu: ProvisionMenu) -> QuerySet[Provision]:
        """Return all dishes attached to menu"""
        raise NotImplementedError()
