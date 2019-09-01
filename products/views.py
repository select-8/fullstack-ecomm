from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.contrib import messages
import django_filters
from .models import Product, Category
from .filters import ProductFilter
from reviews.forms import ReviewForm
from reviews.models import Review


def all_products(request):
    all_products = Product.objects.all()
    category_list = Category.objects.all()

    f = ProductFilter(request.GET, queryset=Product.objects.all())

    paginator = Paginator(all_products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {
        "products": products,
        "filter": f,
        "category_list": category_list,
    }

    return render(request, "products.html", context)

def product_by_cat(request, category_name=None):
    all_products = Product.objects.all()
    categories = Category.objects.all()

    selected_categories = get_object_or_404(Category, category=category_name)
    products_by_cat = Product.objects.filter(category__category=category_name)

    context = {
        'products_by_cat': products_by_cat,
    }

    return render(request, 'filtered_by_cat.html', context)

def product_detail(request, pk):
    '''
    Create a view that returns a single
    Product object based on the product ID (pk) and
    render it to the 'product_detail.html' template
    Or return a 404 if the post is not found.
    '''

    product = get_object_or_404(Product, pk=pk)

    avg_rating = Review.objects.filter(product_id=pk).aggregate(Avg('rating'))

    try:
        reviews = Review.objects.filter(product_id=pk).order_by('-created')
    except:
        reviews = None

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, "Your review has been addeed")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ReviewForm()
    # return render(request, 'reviewform.html', {'form': form})
        
    context = {
        'product': product,
        'avg_rating': avg_rating,
        'reviews': reviews,
        'form': form,
        }
    return render(request, "product_detail.html", context)