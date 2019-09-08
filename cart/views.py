from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from products.models import Product

# Create your views here.


def view_cart(request):
    '''
    A view that renders the cart contents page
    '''
    return render(request, "cart.html")


def add_to_cart(request, id):
    '''Add a quantity of the specified product to the cart'''
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=id)
    current_stock = product.cart_stock
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    print(cart)
    for k, v in cart.items():
        if k == id:
            current_stock -= v
            if current_stock == 0 and id in cart:
                update = Product.objects.filter(
                    id=id).update(cart_stock=current_stock)
                cart[id] = int(cart[id]) + current_stock
                print(cart)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    all_products = Product.objects.all()

    top_sellers = Product.objects.raw(
        "select * from products_product order by sales desc limit 9;")

    context = {
        "top_sellers": top_sellers,
    }


def adjust_cart(request, id):
    '''adjust the quantity of the specified product to the specified amount'''
    product = get_object_or_404(Product, pk=id)
    current_stock = product.cart_stock
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
        for k, v in cart.items():
            if k == id:
                current_stock -= v
                if current_stock == 0:
                    update = Product.objects.filter(
                        id=id).update(cart_stock=current_stock)
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    del cart[id]
    print(cart)
    current_stock = product.stock
    update = Product.objects.filter(id=id).update(cart_stock=current_stock)
    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))