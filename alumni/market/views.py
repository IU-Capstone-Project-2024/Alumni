from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'market/market.html', {'products': products})


# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'myapp/product_detail.html', {'product': product})
