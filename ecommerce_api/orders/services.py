from cart.models import Cart
from products.models import Product
from django.db import transaction
from orders.models import Order, OrderItem


def checkout_cart(user):
    cart = Cart.objects.get(user=user)

    if not cart.items.exists():
        raise ValueError("Cart is empty")

    total = 0
    with transaction.atomic():
        order = Order.objects.create(user=user, total_price=0, status='PENDING')

        for item in cart.items.all():
            if item.product.stock < item.quantity:
                raise ValueError(f"Insufficient stock for product {item.product.name}")

            total += item.quantity * item.product.price

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

            item.product.stock -= item.quantity
            item.product.save()
            item.delete()

        order.total_price = total
        order.save()

    return order
            
