from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Product
from reviews.models import Review

# Create your views here.
def all_products(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 6)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products.html", {"products": products})

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
        reviews = Review.objects.filter(product_id=pk)
    except:
        reviews = None
    context = {
        'product': product,
        'avg_rating': avg_rating,
        'reviews': reviews,
        }
    return render(request, "product_detail.html", context)