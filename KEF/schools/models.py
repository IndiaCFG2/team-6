from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    registered_date = models.DateTimeField(default = timezone.now)

class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    school_id = models.ForeignKey(School, on_delete = models.CASCADE)
