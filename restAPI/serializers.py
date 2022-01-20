from rest_framework import serializers

from restAPI.models import Measurements, MeasurementsSets

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = '__all__'

class MeasurementsSetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementsSets
        fields = '__all__'