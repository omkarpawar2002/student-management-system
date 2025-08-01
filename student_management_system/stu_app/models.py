from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(primary_key=True,help_text="Kindly please enter your roll number")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=15)
    subjects = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    eligible = models.BooleanField(default=False)
    