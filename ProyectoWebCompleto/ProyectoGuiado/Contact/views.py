from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    formulario_contacto = FormularioContacto()
    if request.method=="POST":
        formulario_contacto = FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            email = EmailMessage(
                'Mensaje de Proyecto Web Completo',
                'El usuario con nombre: {} con la dirección {} escribe lo siguiente: \n\n{}'.format(nombre, email, contenido),
                '', 
                ['cursoendjango@gmail.com'], 
                reply_to = [email]
            )
            try:
                email.send()
                return redirect("/contact/?OK")
            except:
                return redirect("/contact/?ERROR")
            
    return render(request, 'contact/contact.html', {'miFormulario': formulario_contacto})
