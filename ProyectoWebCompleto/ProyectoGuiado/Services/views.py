from django.shortcuts import render
from Services.models import Servicio


def services(request):
    ser = Servicio.objects.all()
    return render(request, 'services/services.html', {'servicios': ser})
