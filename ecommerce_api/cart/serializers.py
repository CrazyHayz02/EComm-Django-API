# cart/serializers.py
from rest_framework import serializers
from .models import Product, Cart, CartItem
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    # nested serialization for product details
    product = ProductSerializer(read_only=True)

    # allow setting product by its ID when creating/updating cart items
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "cart", "product", "product_id", "quantity"] 

    # Custom validation for quantity
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be at least 1")
        return value

class CartSerializer(serializers.ModelSerializer):
    # add nested serialization for cart items
    items = CartItemSerializer(many=True, read_only=True)

    # add total price field
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "items", "user", "total_price"]

    # method to calculate total price
    def get_total_price(self, obj):
        return sum([item.product.price * item.quantity for item in obj.items.all()])
