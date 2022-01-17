from rest_framework import viewsets

from restAPI.serializers import MeasurementsSerializer
from restAPI.models import Measurements


class MeasurementsViewSet(viewsets.ModelViewSet):
    queryset = Measurements.objects.all().order_by('timestamp')
    serializer_class = MeasurementsSerializer