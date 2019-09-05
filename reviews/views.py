from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from products.models import Product
from .forms import ReviewForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# Create your views here.
@login_required
def add_a_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return render(request, 'reviewform.html', {'form': form})
    else:
        form = ReviewForm()
    return render(request, 'reviewform.html', {'form': form})
