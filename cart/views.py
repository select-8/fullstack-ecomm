from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    '''
    A view that renders the cart contents page
    '''
    return render(request, "cart.html")

def add_to_cart(request, id):
    '''Add a quantity of the specified product to the cart'''
    quantity=int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=id)
    current_stock = product.stock

    cart = request.session.get('cart', {}) # returns session cart if one exists, an empty dict if no cart exists
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart

    for k, v in cart.items():
        if k == id:
            current_stock -= v

    return redirect(reverse('index'))

def adjust_cart(request, id):
    '''adjust the quantity of the specified product to the specified amount'''
    quantity = int(request.POST.get('quantity')) # get existing quantity
    cart = request.session.get('cart', {}) # get the session cart

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart') 