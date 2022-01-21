from abc import ABC, abstractmethod

import time

from restAPI.models import MeasurementsSets, Measurements


class Camera(ABC):

    @abstractmethod
    def __init__(self, measurements_per_second):
        pass

    @abstractmethod
    def start(self):
        pass

    def write_to_database(obj_array):
        measurementsSets = []
        timestamp_now = time.time().__floor__()
        for element in obj_array:
            measurement_set_id = False
            for x in range(measurementsSets.__len__()):
                if measurementsSets[x].id == element.id:
                    measurement_set_id = x
                    
            if (measurement_set_id == False):
                measurement_set_id = measurementsSets.__len__()
                measurementsSets.append(
                    MeasurementsSets.objects.create(
                        objectID = element.id,
                        complete = False,
                        timestamp = timestamp_now
                    )
                )
            
            Measurements.objects.create(
                object_id=element.id,
                x_position=element.position[0],
                y_position=element.position[1],
                z_position=element.position[2],
                x_velocity=element.velocity[0],
                y_velocity=element.velocity[1],
                z_velocity=element.velocity[2],
                x_dimension=element.dimensions[0],
                y_dimension=element.dimensions[1],
                z_dimension=element.dimensions[2],
                timestamp=(time.time() * 1000).__floor__(),
                measurements_set=measurement_set_id
            )

        for measurementsSet in measurementsSets:
            measurementsSet.complete = True
            measurementsSet.save()
