from django.db import models
from django.utils import timezone


class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    mechanic_name = models.CharField(max_length=200)
    other_mechanic_details = models.TextField(default='')

    def __str__(self):
        return f'{self.mechanic_name} ({self.mechanic_id})'


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    datetime_of_service = models.DateTimeField(default=timezone.now)
    payment_received = models.CharField(max_length=3, choices=[
        ('N', 'No'), ('Y', 'Yes'), ], default='N', blank=False)
    other_booking_details = models.TextField(default='')

    def __str__(self):
        return f'{self.booking_id} for {self.customer} assigned to {self.mechanic}'
