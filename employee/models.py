from django.db import models
from django.utils import timezone



# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.PositiveIntegerField(unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    def formatted_dob(self):
        return self.dob.strftime('%d/%m/%Y')
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    appointment_date = models.DateField()
    def formatted_appointment_date(self):
        return self.appointment_date.strftime('%d/%m/%Y')

    def __str__(self):
        return self.name



