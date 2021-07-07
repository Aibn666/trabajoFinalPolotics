from django.urls import path
from CARRITO import views

#app_name = "Carrito"

urlpatterns = [
    path('', views.carrito, name= "Carrito"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    #path('vaciar/', views.vaciar_carro, name="vaciar"),
]

