from django.contrib import admin
from .models import Servicio


class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'created', 'updated')
    search_fields = ('titulo', 'created', 'updated')
    list_filter = ('titulo', 'created', 'updated')
    date_hierarchy = 'created'
    date_hierarchy = 'updated'
    readonly_fields = ('created', 'updated')


admin.site.register(Servicio, ServicioAdmin)
