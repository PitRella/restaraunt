from rest_framework.viewsets import ModelViewSet
from orders.models import Order
from orders.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    """
    ViewSet for orders.
    """
    queryset = Order.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
    serializer_class = OrderSerializer