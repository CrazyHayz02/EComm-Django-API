from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]
