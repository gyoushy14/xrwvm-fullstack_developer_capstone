from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib import admin

# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # يمكن إضافة حقول أخرى حسب الحاجة

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # علاقة Many-to-One مع CarMake
    name = models.CharField(max_length=100)
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # يمكنك إضافة المزيد من الاختيارات حسب الحاجة
    ]
    
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )
    # يمكن إضافة حقول أخرى حسب الحاجة

    def __str__(self):
        return self.name

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
