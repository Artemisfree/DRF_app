from rest_framework import serializers
from .models import Mappack


class MappackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mappack
        fields = ('id', 'name', 'csv_file', 'json_file', 'a2l_file', 'kp_file')
