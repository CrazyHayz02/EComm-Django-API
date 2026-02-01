from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from .services import checkout_cart



class OrderViewSet(viewsets.ViewSet):
    # Only authenticated users can access orders
    permission_classes = [permissions.IsAuthenticated]

    # GET /orders/ - Retrieve the current user's orders
    def list(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    # POST /orders/checkout/ - Checkout the current user's cart
    @action(detail=False, methods=['post'])
    def checkout(self, request):
        try:
            order = checkout_cart(request.user)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=200)
        except ValueError as exc:
            return Response(
                {"error": str(exc)},
                status=400
            )



