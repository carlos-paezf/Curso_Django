from django.shortcuts import render
from Services.models import Servicio


def home(request):
    return render(request, 'ProjectWebApp/home.html')


def services(request):
    ser = Servicio.objects.all()
    return render(request, 'ProjectWebApp/services.html', {'servicios': ser})


def shop(request):
    return render(request, 'ProjectWebApp/shop.html')


def blog(request):
    return render(request, 'ProjectWebApp/blog.html')


def contact(request):
    return render(request, 'ProjectWebApp/contact.html')
