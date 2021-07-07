from django.urls import path, include
from JAGUARAPP import views
#from CARRITO import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.home, name= "Home"),
    path('info',views.info, name= "Info"),
    path('busqueda',views.busqueda, name= "Busqueda"),
    
    path('contacto',views.contacto, name= "Contacto"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)