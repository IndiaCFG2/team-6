from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=35)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

