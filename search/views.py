from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from products.models import Product, Category


# http://shopnilsazal.github.io/django-pagination-with-basic-search/

def do_search(request):
    product_list = Product.objects.all()
    query = request.GET.get('q')
    if query:
        product_list = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).distinct()
    paginator = Paginator(product_list, 3) # 3 products per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products
    }
    
    amount = len(product_list)
    if amount == 0:
        messages.info(request, 'Unfortunately, your search returned no items.')
        return redirect(reverse('index'))
    elif amount > 0:
        messages.info(request, 'Results: {0} '.format(amount))
        return render(request, "product_filter.html", context)

def cat_filter(request):
    category_list = Category.objects.all()
    product_list = Product.objects.filter(category="Books")
    print(product_list)
    link = request.GET.get('cat-link') # name of input button
    if link:
        product_list = Product.objects.filter(
            Q(category__iexact=link)
        ).distinct()
    paginator = Paginator(product_list, 3) # 3 products per page
    page = request.GET.get('page')

    context = {
        'products': products
    }

    return render(request, "product_filter.html", context)


