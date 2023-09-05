from django.db import models

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=100, default='')
    pais = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=250)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)  # Corregido el argumento on_delete
    especialidad = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
