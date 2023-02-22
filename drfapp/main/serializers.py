from rest_framework import serializers
from .models import CsvData


class CsvDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvData
        fields = '__all__'
