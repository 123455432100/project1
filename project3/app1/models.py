from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(null=True)
    student_name = models.CharField(max_length = 50,null=True)
    student_age = models.IntegerField(null=True)
    student_gender = models.TextField(null=True)
    student_class = models.IntegerField(null=True)