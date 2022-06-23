from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Educator(models.Model):
    educator=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,blank=True)
    
class Student(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    created_by=models.ForeignKey(Educator,on_delete=models.CASCADE)
    images=models.ImageField(upload_to=upload_to, blank=True, null=True)

class Enrolled(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

class Tutorial(models.Model):
    tut_name=models.CharField(max_length=100)
    content=models.TextField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    

