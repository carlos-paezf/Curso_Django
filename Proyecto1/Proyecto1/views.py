from django.http import HttpResponse

def saludo(request):    #Primera Vista
    return HttpResponse("Mi primer programa con el Framework Django")

def despedida(request):
    return HttpResponse("Se han agregado de manera correcta las vistas")
