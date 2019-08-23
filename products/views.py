from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_products(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 3)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products.html", {"products": products})

def product_detail(request, pk):
    '''
    Create a view that returns a single
    post object based on the post ID (pk) and
    render it to the 'postdetail.html' template
    Or return a 404 if the post is not found
    '''

    product = get_object_or_404(Product, pk=pk)
    # product.views += 1
    product.save()
    return render(request, "product_detail.html", {'product': product})