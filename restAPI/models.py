from django.db import models


class Measurement(models.Model):
    objectID = models.IntegerField()
    xPosition = models.DecimalField(max_digits = 5, decimal_places = 3)
    yPosition = models.DecimalField(max_digits = 5, decimal_places = 3)
    zPosition = models.DecimalField(max_digits = 5, decimal_places = 3)
    xVelocity = models.DecimalField(max_digits = 5, decimal_places = 3)
    yVelocity = models.DecimalField(max_digits = 5, decimal_places = 3)
    zVelocity = models.DecimalField(max_digits = 5, decimal_places = 3)
    xDimension = models.DecimalField(max_digits = 5, decimal_places = 3)
    yDimension = models.DecimalField(max_digits = 5, decimal_places = 3)
    zDimension = models.DecimalField(max_digits = 5, decimal_places = 3)
    timestamp = models.IntegerField()

    def __str__(self):
        return self.id
