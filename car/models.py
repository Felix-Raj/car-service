from django.db import models


class Manufacturer(models.Model):
    manufacturer_code = models.CharField(primary_key=True, max_length=300)
    manufacturer_name = models.TextField()
    manufacturer_details = models.TextField(default='')

    def __str__(self):
        return f'{self.manufacturer_name} ({self.manufacturer_code})'


class CarModel(models.Model):
    model_code = models.CharField(primary_key=True, max_length=200)
    daily_hire_rate = models.FloatField()
    model_name = models.CharField(max_length=250)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.model_code} by {str(self.manufacturer)}'


class Car(models.Model):
    license_number = models.CharField(primary_key=True, max_length=250)
    current_mileage = models.FloatField()
    engine_size = models.FloatField()
    other_car_details = models.TextField(default='')
    car_model = models.ForeignKey(to=CarModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.license_number} - {str(self.car_model)}'
