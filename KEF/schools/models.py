from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    registered_date = models.DateTimeField(auto_now_add = True)

class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    school_id = models.ForeignKey(School, on_delete = models.CASCADE)
