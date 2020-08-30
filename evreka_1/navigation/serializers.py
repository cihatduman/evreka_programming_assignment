from rest_framework import serializers
from .models import Vehicle, NavigationRecord


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'plate']


class NavigationRecordSerializer(serializers.HyperlinkedModelSerializer):
    vehicle_plate = serializers.CharField(source='vehicle.plate', read_only=True)

    class Meta:
        model = NavigationRecord
        fields = ['latitude', 'longitude', 'vehicle_plate', 'datetime']
