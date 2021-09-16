from .models import Task
from rest_framework import viewsets, permissions
from .serializer import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]

    serializer_class = TodoSerializer
