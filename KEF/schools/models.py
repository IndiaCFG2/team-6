from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

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


class Courses(models.Model):
    course_name=models.CharField(max_length=200)
    duration=models.TimeField()
    date=models.DateTimeField(default=datetime.now,verbose_name=u"Add time")
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    course_link=models.CharField(max_length=200)
    course_image=models.ImageField(upload_to=None, height_field=None, width_field=None)