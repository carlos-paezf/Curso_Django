from django.shortcuts import render


def home(request):
    return render(request, 'ProjectWebApp/home.html')


def shop(request):
    return render(request, 'ProjectWebApp/shop.html')
