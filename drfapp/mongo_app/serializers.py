from rest_framework import serializers
from .models import Mappack


class MappackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mappack
        fields = '__all__'
