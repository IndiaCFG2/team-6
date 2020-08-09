from django.contrib import admin
from .models import Teacher, School,Courses
# Register your models here.

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Courses)
