from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.AutoField(primary_key=True,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to='student_uploads/' ,null=False,blank=False)
    email=models.EmailField(max_length=25,unique=True)
    address=models.CharField(max_length=25)
    contact = models.CharField(max_length=10)
    dateCreated = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name}{self.last_name}"