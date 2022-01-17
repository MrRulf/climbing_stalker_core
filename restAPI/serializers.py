from rest_framework import serializers

from restAPI.models import Measurement

class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = ('id', 'objectID', 'xPosition', 'yPosition', 'zPosition', 'xVelocity', 'yVelocity', 'zVelocity', 'xDimension', 'yDimension', 'zDimension', 'timestamp')