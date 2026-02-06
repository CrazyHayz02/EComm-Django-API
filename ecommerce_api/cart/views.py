from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from .services import add_to_cart, remove_from_cart

class CartViewSet(viewsets.ViewSet):
    # Only authenticated users can access the cart
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer

    # GET /cart/ - Retrieve the current user's cart
    def list(self, request):
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    # POST /cart/add/ - Add an item to the cart
    @action(detail=False, methods=['post'])
    def add(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        add_to_cart(request.user, product_id, quantity)
        return Response({'status': 'added'})

    # POST /cart/remove/ - Remove an item from the cart
    @action(detail=False, methods=['post'])
    def remove(self, request):
        product_id = request.data.get('product_id')
        remove_from_cart(request.user, product_id)
        return Response({'status': 'removed'})