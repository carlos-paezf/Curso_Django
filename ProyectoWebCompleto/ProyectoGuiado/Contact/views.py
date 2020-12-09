from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.


def contact(request):
    formulario_contacto = FormularioContacto()
    return render(request, 'contact/contact.html', {'miFormulario': formulario_contacto})