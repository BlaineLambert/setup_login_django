from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    number = models.IntegerField()
    email = models.EmailField()