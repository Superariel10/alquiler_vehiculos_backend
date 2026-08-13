from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Alquiler, Vehiculo
from .serializers import AlquilerSerializer, VehiculoSerializer
from .permissions import IsAdminOrReadOnly

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all().order_by("id")
    serializer_class = VehiculoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["brand", "plate"]
    ordering_fields = ["id", "brand", "plate", "daily_rate", "is_available"]

class AlquilerViewSet(viewsets.ModelViewSet):
    queryset = Alquiler.objects.select_related("id_vehiculo").all().order_by("-id")
    serializer_class = AlquilerSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["id_vehiculo", "status"]
    search_fields = ["customer_name", "total", "status", "created_at"]
    ordering_fields = ["id", "customer_name", "total", "status", "created_at"]

    def get_queryset(self):
        qs = super().get_queryset()
        anio_min = self.request.query_params.get("anio_min")
        anio_max = self.request.query_params.get("anio_max")
        if anio_min:
            qs = qs.filter(anio__gte=int(anio_min))
        if anio_max:
            qs = qs.filter(anio__lte=int(anio_max))
        return qs

    def get_permissions(self):
        # Público: SOLO listar vehículos
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()