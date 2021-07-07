from django.shortcuts import render, HttpResponse
from PRODUCTO.models import Producto
# Create your views here.

def home(request):
    productos=Producto.objects.all()
    return render(request, "JAGUARAPP/modelo.html",{
        "productos": productos
    })

def info(request):
    
    return render(request, "JAGUARAPP/Info.html")

def busqueda(request):
    
    return render(request, "JAGUARAPP/Busqueda.html")

#def login(request):
    
#    return render(request, "USUARIOS/Login.html")

#def registro(request):
    
    return render(request, "USUARIOS/Registro.html")


def contacto(request):
    
    return render(request, "JAGUARAPP/Contacto.html")