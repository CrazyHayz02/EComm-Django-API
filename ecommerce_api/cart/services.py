from .models import Cart, CartItem
from products.models import Product
from django.db import transaction

def add_to_cart(user, product_id, quantity=1):
    try: 
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise ValueError("Product does not exist")
    
    if product.stock < quantity:
        raise ValueError("Insufficient stock")
    
    with transaction.atomic():
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
    return cart_item


def remove_from_cart(user, product_id, quantity=1):
    try:
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        raise ValueError("Item not in cart")
    
    with transaction.atomic():
        if cart_item.quantity <= quantity:
            cart_item.delete()
        else:
            cart_item.quantity -= quantity
            cart_item.save()
    return cart_item
