from rest_framework import serializers
from .models import Alquiler, Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ["id_vehiculo", "plate", "brand", "daily_rate", "is_available"]

class AlquilerSerializer(serializers.ModelSerializer):
    alquiler_nombre = serializers.CharField(source="vehiculo.brand", read_only=True)

    class Meta:
        model = Alquiler
        fields = ["id_alquiler", "id_vehiculo", "customer_name", "alquiler_nombre", "total", "status", "created_at"]