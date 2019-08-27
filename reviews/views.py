from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from products.models import Product
from .forms import ReviewForm

# Create your views here.
def add_a_review(request, pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            return redirect(product_detail, review.pk)
    else:
        form = ReviewForm()
    return render(request, 'reviewform.html', {'form': form})



