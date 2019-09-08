from django.shortcuts import render
from products.models import Product, Category


def top_products(request):
    all_products = Product.objects.all()

    top_toys = Product.objects.raw(
        "select * from products_product where category_id = 1 order by sales desc limit 3;")

    top_comics = Product.objects.raw(
        "select * from products_product where category_id = 2 order by sales desc limit 3;")

    top_books = Product.objects.raw(
        "select * from products_product where category_id = 3 order by sales desc limit 3;")

    context = {
        "top_toys": top_toys,
        "top_comics": top_comics,
        "top_books": top_books,
    }

    return render(request, "home.html", context)
