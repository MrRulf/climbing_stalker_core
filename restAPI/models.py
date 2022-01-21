from django.db import models


class MeasurementsSets(models.Model):
    object_id = models.IntegerField(null = False)
    complete = models.BooleanField(null = False, default = False)
    timestamp = models.IntegerField(null = False)

    def __str__(self):
        return str(self.id)

class Measurements(models.Model):
    x_position = models.DecimalField(max_digits = 5, decimal_places = 3, null = False)
    y_position = models.DecimalField(max_digits = 5, decimal_places = 3, null = False)
    z_position = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    x_velocity = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    y_velocity = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    z_velocity = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    x_dimension = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    y_dimension = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    z_dimension = models.DecimalField(max_digits = 5, decimal_places = 3, null = True)
    timestamp = models.IntegerField(null = False)
    measurements_set = models.ForeignKey(MeasurementsSets, on_delete = models.RESTRICT, null = False)

    def __str__(self):
        return str(self.id)