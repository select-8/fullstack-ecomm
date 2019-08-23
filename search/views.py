from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from products.models import Product

# Create your views here.

# def do_search(request):
#     products = Product.objects.filter(name__icontains=request.GET['q'])
#     if len(products) == 0:
#         messages.info(request, "We dont got that")
#         return redirect(reverse('index'))
#     else:
#         return render(request, 'products.html', {"products": products})

def do_search(request):
    product_list = Product.objects.all()
    query = request.GET.get('q')
    if query:
        product_list = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).distinct()
    paginator = Paginator(product_list, 3) #
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products
    }
    return render(request, "product_filter.html", context)