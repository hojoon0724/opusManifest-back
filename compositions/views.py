from .models import Composition
from rest_framework import viewsets, permissions
from .serializers import CompositionSerializer


class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
    permission_classes = [permissions.AllowAny]
