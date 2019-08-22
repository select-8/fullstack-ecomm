from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.

def view_cart(request):
    '''
    A view that renders the cart contents page
    '''
    return render(request, "cart.html")

def add_to_cart(request, id):
    '''Add a quantity of the specified product to the cart'''
    quantity=int(request.POST.get('quantity'))

    cart = request.session.get('cart', {}) # returns session cart if one exists, an empty dict if no cart exists
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
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
