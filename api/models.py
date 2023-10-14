from django.db import models

# Create your models here.

class Pessoa(models.Model):
    age = models.IntegerField()
    cpf = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    income = models.FloatField()
    location = models.CharField(max_length=20)



