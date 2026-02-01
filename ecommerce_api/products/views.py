from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly
from .throttles import ProductWriteThrottle

    

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Only admin users can create, update, or delete products
    permission_classes = [IsAdminOrReadOnly]

    # Throttle write operations to 5 per minute per user
    throttle_classes = [ProductWriteThrottle]

    filterset_fields = ["price", "stock"]
    ordering_fields = ["price", "created_at"]