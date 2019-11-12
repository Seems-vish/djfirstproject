from django.db import models

# Create your models here.

class Student(models.Model):
    studName=models.CharField('stud_name',max_length=100)
    studAge = models.IntegerField('stud_age')
    studAddress = models.CharField('stud_address',max_length=100)
    studCollege = models.CharField('stud_college',max_length=100)
    studEmail = models.EmailField('stud_email',unique=True,max_length=100)
    studDept = models.CharField('stud_dept',max_length=100)
#Student(studName='AAA',studAge=29,studAddress='Pune',studCollege='XXX',studEmail='abc@gmail.com',studDept='IT')
    class Meta:
        db_table = "student"  