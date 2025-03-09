from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import ActionLog
from .serializers import ActionLogSerializer

# Create your views here.

class ActionLogViewSet(viewsets.ModelViewSet):
    queryset = ActionLog.objects.all()
    serializer_class = ActionLogSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset = ['user', 'timestamp']
    ordering_fields = ['timestamp']
    ordering = ['-timestamp']
