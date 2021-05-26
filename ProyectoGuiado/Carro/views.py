from django.shortcuts import render
from Carro.carro import Carro
from Shop.models import Product
from django.shortcuts import redirect

# Create your views here.


def add_product(request, product_id):
    carro = Carro(request)
    product = Product.objects.get(id = product_id)
    carro.add_product(product = product)
    return redirect("Shop")


def delete_product(request, product_id):
    carro = Carro(request)
    product = Product.objects.get(id = product_id)
    carro.delete_product(product= product)
    return redirect("Shop")


def substract_units_product(request, product_id):
    carro = Carro(request)
    product = Product.objects.get(id = product_id)
    carro.substract_units_product(product = product)
    return redirect("Shop")


def clean_carro(request):
    carro = Carro(request)
    carro.clean_carro()
    return redirect("Shop")
