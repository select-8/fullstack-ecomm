from django.shortcuts import render
from products.models import Product, Category

def top_products(request):
    all_products = Product.objects.all()

    top_sellers = Product.objects.raw(
        "select * from products_product order by sales desc limit 9;")

    context = {
        "top_sellers": top_sellers,
    }

    return render(request, "home.html", context)
