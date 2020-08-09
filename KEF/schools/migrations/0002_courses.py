# Generated by Django 3.1 on 2020-08-09 02:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('duration', models.TimeField()),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Add time')),
                ('description', models.CharField(max_length=500)),
                ('course_link', models.CharField(max_length=200)),
                ('course_image', models.ImageField(upload_to=None)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.teacher')),
            ],
        ),
    ]
