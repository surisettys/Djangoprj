from django.db import models

# Create your models here.

class Patient(models.Model):

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    hospital_name = models.CharField(max_length=30)
    info = models.CharField(max_length=250)

    def __str__(self):

        return f'{self.name} is {self.age} old admitted to {self.hospital_name}'
