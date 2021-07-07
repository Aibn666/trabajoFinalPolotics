from django.shortcuts import render
from .models import * 
from .forms import UserRegisterForm 
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def login(request):
    
    return render(request, "registration/Login.html")

def logout(request):
    
    return render(request, "registration/Login.html")

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')

    else:
        form = UserRegisterForm ()

    context = {'form': form}
    return render(request, "registration/Registro.html",context)   
