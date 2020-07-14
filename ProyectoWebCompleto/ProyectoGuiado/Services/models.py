from django.db import models


class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='services')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.titulo

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'
