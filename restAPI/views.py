from django.http import HttpResponse, JsonResponse

from restAPI.serializers import MeasurementsSetsSerializer, MeasurementsSerializer
from restAPI.models import Measurements, MeasurementsSets

# makes migrations crash


def measurements_sets_latest(request):
    basename = 'measurements-sets-latest'
    try:
        queryset = MeasurementsSets.objects.all()
        queryset = queryset.filter(complete=True)
        queryset = queryset.order_by('timestamp')
        queryset = queryset.filter(timestamp=queryset.first().timestamp)
    except MeasurementsSets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MeasurementsSetsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    return HttpResponse(status=405)


def measurements_sets_id(request, pk):
    basename = 'measurements-sets-id'
    try:
        queryset = MeasurementsSets.objects.get(pk=pk)
    except MeasurementsSets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MeasurementsSetsSerializer(queryset)
        return JsonResponse(serializer.data)


def measurements_sets(request):
    basename = 'measurements-sets'
    try:
        queryset = MeasurementsSets.objects.all()
    except MeasurementsSets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MeasurementsSetsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status=204)

    return HttpResponse(status=405)


def measurements_latest(request):
    basename = 'measurements-latest'
    try:
        measurements_set_id_latest = MeasurementsSets.objects.all()
        measurements_set_id_latest = measurements_set_id_latest.filter(
            complete=True)
        measurements_set_id_latest = measurements_set_id_latest.order_by(
            'timestamp')
        measurements_set_id_latest = measurements_set_id_latest.first()
        measurements_set_id_latest = measurements_set_id_latest.id
        queryset = Measurements.objects.all()
        queryset = queryset.filter(measurementsSet=measurements_set_id_latest)
        queryset = queryset.order_by('timestamp')
    except (MeasurementsSets.DoesNotExist, Measurements.DoesNotExist):
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MeasurementsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    return HttpResponse(status=405)


def measurements_id(request, pk):
    basename = 'measurements-id'
    try:
        queryset = Measurements.objects.get(pk=pk)
    except Measurements.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MeasurementsSerializer(queryset)
        return JsonResponse(serializer.data)


def measurements(request):
    basename = 'measurements'
    try:
        queryset = Measurements.objects.all()
    except Measurements.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MeasurementsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status=204)

    return HttpResponse(status=405)
