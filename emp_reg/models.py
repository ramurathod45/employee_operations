from django.db import models

# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=30, default='Guest')
    phone_num = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=30)
    joiningDate = models.DateField()

    class Meta:
        db_table = 'EMPLOYEE_MASTER'
        ordering = ['role']
