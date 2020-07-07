from django.contrib import admin
from gestionPedidos.models import *

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")
    search_fields = ("nombre", "telefono")

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "seccion", "precio")
    list_filter = ("seccion", "precio")
    search_fields = ("nombre",)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha", "entregado")
    list_filter = ("fecha", "entregado")
    date_hierarchy = "fecha"
    search_fields = ("entregado",)

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
