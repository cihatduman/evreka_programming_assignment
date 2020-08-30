from datetime import datetime, timedelta
from rest_framework import permissions, viewsets, status
from .models import NavigationRecord, Vehicle
from .serializers import NavigationRecordSerializer, VehicleSerializer


class LatestRecordViewSet(viewsets.ModelViewSet):
    queryset = NavigationRecord.objects.filter(datetime__gte=datetime.now() - timedelta(days=2))\
            .order_by('vehicle_id', 'datetime').distinct('vehicle')
    serializer_class = NavigationRecordSerializer
    permission_classes = [permissions.AllowAny]


class RecordViewSet(viewsets.ModelViewSet):
    queryset = NavigationRecord.objects.all()
    serializer_class = NavigationRecordSerializer
    permission_classes = [permissions.AllowAny]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.AllowAny]
