from rest_framework import viewsets

from restAPI.serializers import MeasurementSerializer
from restAPI.models import Measurement


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all().order_by('timestamp')
    serializer_class = MeasurementSerializer