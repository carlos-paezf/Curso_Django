from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["producto"]:
        # mensaje = "Articulo Buscado: %s" % request.GET["producto"]
        producto = request.GET["producto"]
        if len(producto)>20:
            mensaje = "Limite de caracteres excedido"
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busqueda.html", {"articulos": articulos,
                                                                "query": producto})
    else:
        mensaje = "No hay criterio de busqeda"
    return HttpResponse(mensaje)

def formulario_contacto(request):
    if request.method == "POST":
        return render(request, "gracias.html")
    return render(request, "formulario_contacto.html")
