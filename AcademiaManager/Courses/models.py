from django.db import models

# Create your models here.
from django.db import models
from Teachers.models import Teacher
from Students.models import Student

class Course(models.Model):
    code = models.CharField(primary_key=True,max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
    students = models.ManyToManyField(Student, related_name='courses')
    semester = models.IntegerField(Student, related_name='courses')
    

    def __str__(self):
        return f"{self.name} ({self.code})"
