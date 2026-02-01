from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from orders.views import OrderViewSet
from cart.views import CartViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet , basename='products')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = router.urls