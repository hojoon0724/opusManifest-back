from .models import Composition
from rest_framework import serializers


class CompositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Composition
        fields = "__all__"
