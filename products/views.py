from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import ReviewForm

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
    Product object based on the product ID (pk) and
    render it to the 'product_detail.html' template
    Or return a 404 if the post is not found.
    '''

    product = get_object_or_404(Product, pk=pk)
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
    else:
        form = ReviewForm(instance=review)

    product.views += 1
    product.save()

    context = {
        'product': product,
        'review': review,
        'form': form,
        }
    return render(request, "product_detail.html", context)

# def review_a_product(request, pk=None):
#     review = get_object_or_404(Review, pk=pk) if pk else None
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, request.FILES, instance=review)
#         if form.is_valid():
#             review = form.save()
#             return redirect(product_detail, review.pk)
#     else:
#         form = ReviewForm(instance=review)
#     return render(request, 'product_detail.html', {'form': form})
