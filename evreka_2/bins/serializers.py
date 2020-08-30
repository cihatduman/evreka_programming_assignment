from rest_framework import serializers
from .models import Bin, Operation, BinOperation


class OperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operation
        fields = ['id', 'name']


class BinSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bin
        fields = ['id', 'latitude', 'longitude']


class BinOperationSerializer(serializers.HyperlinkedModelSerializer):
    operation_name = serializers.CharField(source='operation.name', read_only=True)
    bin_latitude = serializers.CharField(source='bin.latitude', read_only=True)
    bin_longitude = serializers.CharField(source='bin.longitude', read_only=True)

    class Meta:
        model = BinOperation
        fields = ['operation_name', 'bin_id', 'operation_frequency', 'last_operation', 'bin_latitude', 'bin_longitude']
