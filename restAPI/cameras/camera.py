from abc import ABC

import time

from restAPI.models import MeasurementsSets, Measurements


class Camera(ABC):

    def write_to_database(obj_array):
        measurementsSet = MeasurementsSets.objects.create(
            complete = False,
            timestamp = time.time().__floor__()
        )
        for element in obj_array:
            Measurements.objects.create(
                objectID = element.id,
                xPosition = element.position[0],
                yPosition = element.position[1],
                zPosition = element.position[2],
                xVelocity = element.velocity[0],
                yVelocity = element.velocity[1],
                zVelocity = element.velocity[2],
                xDimension = element.dimensions[0],
                yDimension = element.dimensions[1],
                zDimension = element.dimensions[2],
                timestamp = (time.time() * 1000).__floor__(),
                measurementsSet=measurementsSet.id
            )
            measurementsSet.complete = True
            measurementsSet.save()