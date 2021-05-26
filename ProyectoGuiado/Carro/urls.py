from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name="add"),
    path('delete/<int:product_id>/', views.delete_product, name="delete"),
    path('substract/<int:product_id>/', views.substract_units_product, name="substract"),
    path('clean/<int:product_id>/', views.clean_carro, name="clean"),
]
