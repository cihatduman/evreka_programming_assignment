from rest_framework import viewsets, permissions
from .serializers import BinSerializer, BinOperationSerializer, OperationSerializer
from .models import Bin, BinOperation, Operation


class BinViewSet(viewsets.ModelViewSet):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer
    permission_classes = [permissions.AllowAny]


class BinOperationViewSet(viewsets.ModelViewSet):
    queryset = BinOperation.objects.all()
    serializer_class = BinOperationSerializer
    permission_classes = [permissions.AllowAny]


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    permission_classes = [permissions.AllowAny]

