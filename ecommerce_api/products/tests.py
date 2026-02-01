from django.test import TestCase
from .models import Product, Cart
from ..cart.services import add_to_cart

class CartTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Book", price=10, stock=5)
        self.user = User.objects.create_user("testuser", "pass")

    def test_add_to_cart(self):
        cart_item = add_to_cart(self.user, self.product.id, 2)
        self.assertEqual(cart_item.quantity, 2)
