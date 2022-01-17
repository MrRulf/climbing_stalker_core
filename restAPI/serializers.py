from rest_framework import serializers

from restAPI.models import Measurements

class MeasurementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurements
        fields = ('id', 'objectID', 'xPosition', 'yPosition', 'zPosition', 'xVelocity', 'yVelocity', 'zVelocity', 'xDimension', 'yDimension', 'zDimension', 'timestamp')