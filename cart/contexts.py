'''
Contexts need to be added to 'context_processors' under TEMPLATES in settings.py
Context_processors are a list of things that are available on every webpage.
'''
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    '''
    Ensures that the cart contents are available when rendering every page
    '''
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    current_stock = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        current_stock = product.cart_stock
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product, 'current_stock': current_stock })

    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count, 'current_stock': current_stock }