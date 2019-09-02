from django.shortcuts import render
from products.models import Product, Category

def top_products(request):
    all_products = Product.objects.all()
    category_list = Category.objects.all()
    top_sales = (Product.objects
                     .order_by('-sales')
                     .values_list('sales', flat=True))
    top_products = (Product.objects
                      .order_by('-sales')
                      .filter(sales__in=top_sales[:3]))
    
    toy_products = Product.objects.filter(category_id=1, sales__in=top_sales[:3])
    comic_products = Product.objects.filter(category_id=2, sales__in=top_sales[:3])
    book_products = Product.objects.filter(category_id=3, sales__in=top_sales[:3])

    context = {
        "top_products": top_products,
        "all_products": all_products,
        "toy_products": toy_products,
        "book_products": book_products,
        "comic_products": comic_products,
    }

    return render(request, "home.html", context)
