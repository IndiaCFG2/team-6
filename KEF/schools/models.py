from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime

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

    def __str__(self):
        return self.user.username

class Courses(models.Model):
    course_name=models.CharField(max_length=200)
    duration=models.TimeField()
    date=models.DateTimeField(default=datetime.now,verbose_name=u"Add time")
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    course_link=models.CharField(max_length=200)

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = Teacher.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=User)