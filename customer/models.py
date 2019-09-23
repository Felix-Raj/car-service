from django.db import models


class Customer(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'), (FEMALE, 'Female'), (OTHERS, 'Others')
    ]
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15)
    email_address = models.EmailField()
    phone_number = models.IntegerField(help_text='Use country code, avoid "+"')
    address_line_1 = models.CharField(max_length=300)
    address_line_2 = models.CharField(max_length=300)
    address_line_3 = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    other_customer_details = models.TextField(default='')

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.name} ({self.pk})'
