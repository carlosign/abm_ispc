from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
 

class Categoria(models.Model):

    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(max_length=1000, blank=False)
    class Meta:
        db_table="Categoria"
        verbose_name="Categoria de productos"
        verbose_name_plural="Categorias"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    codigodeBarras = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(max_length=1000, blank=False)
    peso = models.DecimalField(max_length=10, blank=False, decimal_places=2, max_digits=10)
    precio = models.DecimalField(max_length=10, blank=False, decimal_places=2, max_digits=10)
    cantidad = models.PositiveIntegerField(blank=False, default=0)
    id_categoria = models.ForeignKey(Categoria,to_field="id_categoria",on_delete=models.CASCADE)
    class Meta:
        db_table = "Producto"
        verbose_name="Productos de mi kiosco"
        verbose_name_plural="Productos"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre   
    
class CarritoCompras(models.Model):
        producto_nombre = models.CharField(max_length=200)
        producto_precio = models.DecimalField(max_length=10, blank=False, decimal_places=2, max_digits=10)
        producto_cantidad = models.PositiveIntegerField()