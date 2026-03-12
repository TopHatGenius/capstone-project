from django.db import models
# Not in use at the moment - from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # more here if needed

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('MINIVAN', 'Minivan'),
        ('TRUCK', 'Truck'),
    ]
    type = models.CharField(max_length=100, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2025,
                               validators=[
                                   MaxValueValidator(2025),
                                   MinValueValidator(2013)
                               ])

    def __str__(self):
        return self.name  # Returns name as string representation
