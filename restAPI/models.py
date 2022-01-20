from django.db import models


class MeasurementsSets(models.Model):
    complete = models.BooleanField(null = False, default = False)
    timestamp = models.IntegerField(null = False)

    def __str__(self):
        return str(self.id)

class Measurements(models.Model):
    objectID = models.IntegerField(null = False)
    xPosition = models.DecimalField(max_digits = 5, decimal_places = 3, null = False)
    yPosition = models.DecimalField(max_digits = 5, decimal_places = 3, null = False)
    zPosition = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    xVelocity = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    yVelocity = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    zVelocity = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    xDimension = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    yDimension = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    zDimension = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    timestamp = models.IntegerField(null = False)
    measurementsSet = models.ForeignKey(MeasurementsSets, on_delete = models.RESTRICT, null = False)

    def __str__(self):
        return str(self.id)