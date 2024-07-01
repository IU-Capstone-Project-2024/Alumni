# Create your views here.
# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Product
from django.conf import settings


def product_list(request):
    products = Product.objects.all()
    return render(request, 'market/market.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        selected_size = request.POST.get('size')
        request.session['selected_size'] = selected_size
        request.session['product_id'] = product_id
        return redirect('product_buy', product_id=product_id)

    return render(request, 'market/product_details.html', {'product': product})


def product_buy(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    selected_size = request.session.get('selected_size')
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        payment_method = request.POST.get('payment_method')

        send_mail(
            name + " " + surname + " purchase",
            "Your order has been successfully accepted, go to "
            "room 319 and give the employee your first and last name.",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        send_mail(
            name + " " + surname + " purchase",
            "Ordering: " + product.name + "\nMethod of Payment: " + payment_method,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return redirect('checkout')
    return render(request, 'market/product_buy.html', {'product': product, 'selected_size': selected_size})


def checkout(request):
    product_id = request.session.get('product_id')
    price = get_object_or_404(Product, id=product_id).price
    return render(request, 'market/gratitude_buy.html', context={'price': price})