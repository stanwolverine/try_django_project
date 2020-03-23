from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DecimalField()  # in months
    price = models.PositiveSmallIntegerField()  # INR Values from 0 to 32767
    discount = models.DecimalField()  # in percentage
    tutor = models.CharField(max_length=100)
