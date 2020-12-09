from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Tu nombre", required=True, max_length=100)
    email = forms.CharField(label="Email", required=True)
    contenido = forms.CharField(label="Contenido")