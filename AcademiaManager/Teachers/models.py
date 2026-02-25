from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo=models.ImageField(upload_to='teacher_uploads/' ,null=False,blank=False)
    email=models.EmailField(max_length=25,unique=True)
    address=models.CharField(max_length=25)
    phone = models.CharField(max_length=15, blank=True, null=True)

    dateCreated = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name}{self.last_name}"