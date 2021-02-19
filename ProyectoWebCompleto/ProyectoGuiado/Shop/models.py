from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'productCategory'
        verbose_name_plural = 'productCategories'
        
    def __str__(self):
        return self.nombre
    

class Product(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="shop", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
