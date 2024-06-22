from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.product_list),
=======
    path("", views.product_list, name="product_list"),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/buy_<int:product_id>/', views.product_buy, name='product_buy'),
    path('checkout/', views.checkout, name='checkout'),
>>>>>>> origin/master
]
