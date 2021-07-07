from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

from .carrito import Carrito
from PRODUCTO.models import Producto
from django.shortcuts import redirect
# Create your views here.

def carrito(request):
    return render(request, "carrito/Carrito.html")
    

def agregar_producto(request, producto_id):
    carro=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)

    return redirect("Carrito")

def eliminar_producto(request, producto_id):
    carro=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)

    return redirect("Carrito")

def restar_producto(request, producto_id):
    carro=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)

    return redirect("Carrito")

#def vaciar_carro(request):
    carro=Carrito(request)
    carro.vaciar_carro()

    return redirect("Carrito")
