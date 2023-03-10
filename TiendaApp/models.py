from django.db import models

# Create your models here.

class Categoria_Producto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'categoriaProd'
        verbose_name_plural = 'categoriasProd'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    Categorias = models.ForeignKey(Categoria_Producto, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to= 'Tienda', null=True, blank=True)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'