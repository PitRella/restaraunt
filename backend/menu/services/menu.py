from asgiref.sync import sync_to_async
from django.db.models import QuerySet
from menu.abstract import MenuService
from menu.models import ProvisionMenu, Provision


class MenuServiceImpl(MenuService):

    @staticmethod
    @sync_to_async
    def get_dishes_from_menu(menu: ProvisionMenu) -> QuerySet[Provision]:
        """Returns dishes from menu."""
        return menu.dishes.all()

