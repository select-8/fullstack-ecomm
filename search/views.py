from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from products.models import Product

# Create your views here.

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    if len(products) == 0:
        messages.info(request, "We dont got that")
        return redirect(reverse('index'))
    else:
        return render(request, 'products.html', {"products": products})

