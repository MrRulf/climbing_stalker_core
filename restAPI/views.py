from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

from restAPI.serializers import MeasurementsSetsSerializer, MeasurementsSerializer
from restAPI.models import Measurements, MeasurementsSets

# makes migrations crash
def measurementsSetsLatest(request):
    basename = 'measurements-sets-latest'
    try: 
        queryset = MeasurementsSets.objects.all()
        queryset = queryset.filter(complete = True)
        queryset = queryset.order_by('timestamp')
        queryset = queryset.first()
    except MeasurementsSets.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = MeasurementsSetsSerializer(queryset)
        return JsonResponse(serializer.data)
    
    return HttpResponse(status = 405)


def measurementsSetsId(request, pk):
    basename = 'measurements-sets-id'
    try:
        queryset = MeasurementsSets.objects.get(pk = pk)
    except MeasurementsSets.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == 'GET':
        serializer = MeasurementsSetsSerializer(queryset)
        return JsonResponse(serializer.data)


def measurementsSets(request):
    basename = 'measurements-sets'
    try:
        queryset = MeasurementsSets.objects.all()
    except MeasurementsSets.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = MeasurementsSetsSerializer(queryset, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status = 204)
    
    return HttpResponse(status = 405)


def measurementsLatest(request):
    basename = 'measurements-latest'
    try: 
        measurementsSetIdLatest = MeasurementsSets.objects.all()
        measurementsSetIdLatest = measurementsSetIdLatest.filter(complete = True)
        measurementsSetIdLatest = measurementsSetIdLatest.order_by('timestamp')
        measurementsSetIdLatest = measurementsSetIdLatest.first()
        measurementsSetIdLatest = measurementsSetIdLatest.id
        queryset = Measurements.objects.all()
        queryset = queryset.filter(measurementsSet = measurementsSetIdLatest)
        queryset = queryset.order_by('timestamp')
    except (MeasurementsSets.DoesNotExist, Measurements.DoesNotExist):
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = MeasurementsSerializer(queryset, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    return HttpResponse(status = 405)


def measurementsId(request, pk):
    basename = 'measurements-id'
    try:
        queryset = Measurements.objects.get(pk = pk)
    except Measurements.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == 'GET':
        serializer = MeasurementsSerializer(queryset)
        return JsonResponse(serializer.data)


def measurements(request):
    basename = 'measurements'
    try:
        queryset = Measurements.objects.all()
    except Measurements.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = MeasurementsSerializer(queryset, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status = 204)
    
    return HttpResponse(status = 405)
