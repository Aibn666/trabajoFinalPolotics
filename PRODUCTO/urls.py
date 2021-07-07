from django.urls import path
from PRODUCTO import views


urlpatterns = [
    path('',views.producto, name= "Producto"),
    #path('',views.carro, name="Carro"),
]
