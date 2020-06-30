from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):    #Primera Vista
    #Plantilla
    doc_externo = open("D:/Curso_Django/Proyecto1/Proyecto1/plantillas/saludo.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def despedida(request):
    documento = '''
    <html>
        <body>
            <h1>
                Se han agregado de manera correcta las vistas. Esta es una
                de las maneras mas rusticas y no optimas de agregar las cadenas
                de texto
            </h1>
        </body>
    </html>'''
    return HttpResponse(documento)

def fecha(request):
    fecha_actual = datetime.datetime.now()
    doc_externo = open("D:/Curso_Django/Proyecto1/Proyecto1/plantillas/fecha.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"fecha_actual":fecha_actual})
    cuerpo = plantilla.render(contexto)
    return HttpResponse(cuerpo)

def calcularEdad (request,edad,agno):  #Primera URL con parametro
    #Creacion de objeto
    persona1 = Persona("David", "Ferrer")
    #Calculos de la edad
    periodo = agno-2020
    edadFutura = edad+periodo
    #Plantilla
    doc_externo = open("D:/Curso_Django/Proyecto1/Proyecto1/plantillas/calcular_edad.html")
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"edad":edad,
                        "agno":agno,
                        "edad_futura":edadFutura,
                        "nombre":persona1.nombre,
                        "apellido":persona1.apellido})
    cuerpo = plantilla.render(contexto)
    return HttpResponse(cuerpo)
