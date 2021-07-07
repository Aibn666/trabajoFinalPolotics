from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__ (self):
        return self.nombre

class Producto(models.Model):
    titulo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='producto')
    descripcion=models.CharField(max_length=65)
    precio=models.FloatField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.titulo