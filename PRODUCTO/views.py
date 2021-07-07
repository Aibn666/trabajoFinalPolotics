import PRODUCTO
from django.http.response import HttpResponse
from django.shortcuts import render
from PRODUCTO.models import Producto
from django import forms
from django.urls import reverse
# Create your views here.

def producto(request):
    producto=Producto.objects.all()
    return render(request, 'producto/Producto.html',{
        "productos": producto
    })

def carro(request):
    return render(request,'producto/Producto.html')

#class FormAltaProducto(forms.Form):
    producto = forms.CharField(label="nuevo producto")

#def producto(request):
    if "productos" not in request.session:
        request.session["productos"] = []
    return render(request, "PRODUCTO/Producto.html",{
        "productos": request.session["productos"]
    })

#def agregar(request):

    if request.method == "POST":
        form = FormAltaProducto(request.POST)
        if form.is_valid():
            producto = form.cleaned_data["producto"]
            request.session["producto"] += [producto]
            return HttpResponse(reverse('PRODUCTO:Producto'))
        else:
            return render(request, "PRODUCTO/agregar.html")
    else:
        return render(request, "PRODUCTO/agregar.html")
