from django.urls import path, include
from .import views
from django.contrib.auth.views import LoginView, logout_then_login


urlpatterns = [
    #path('',views.login, name= "Login"),
    #path('accounts/',include('django.contrib.auth.urls')),
    path('Registro/', views.registro, name= "Registro"),
    path('Login/', LoginView.as_view(template_name='registration/Login.html'), name='Login'),
    path('Logout/', logout_then_login, name='Logout'),
    
]
