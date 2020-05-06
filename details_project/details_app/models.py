from django.db import models
class Details(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    mob_number = models.CharField(max_length=10,unique=True)
# Create your models here.
