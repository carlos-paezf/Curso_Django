from django.http import HttpResponse
import datetime

def saludo(request):    #Primera Vista
    return HttpResponse("<html><body><h1>Mi primer programa con el Framework Django</h1></body></html>")

def despedida(request):
    documento = '''
    <html>
        <body>
            <h1>
                Se han agregado de manera correcta las vistas
            </h1>
        </body>
    </html>'''
    return HttpResponse(documento)

def fecha(request):
    fecha_actual = datetime.datetime.now()
    cuerpo = '''
    <html>
        <body>
            <h1>
                Fecha y hora actuales %s
            </h1>
        </body>
    </html>''' % fecha_actual
    return HttpResponse(cuerpo)

def calcularEdad (request,edad,agno):  #Primera URL con parametro
    periodo = agno-2020
    edadFutura = edad+periodo
    cuerpo = '''
    <html>
        <body>
            <h1>
                En el año %s tendras %s años
            </h1>
        </body>
    </html>''' %(agno,edadFutura)
    return HttpResponse(cuerpo)
