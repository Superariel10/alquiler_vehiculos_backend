from django.db import models

class Vehiculo(models.Model):
    id_vehiculo = models.CharField(max_length=120, unique=True)
    plate = models.CharField(max_length=20, unique=True)
    brand = models.CharField(max_length=120)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.brand

class Alquiler(models.Model):
    id_alquiler = models.CharField(max_length=120, unique=True)
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT, related_name="alquileres")
    customer_name = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_vehiculo.brand} {self.customer_name} ({self.total})"