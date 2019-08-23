from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 2)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products.html", {"products": products})