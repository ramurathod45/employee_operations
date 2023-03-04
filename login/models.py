from django.db import models

# Create your models here.

class LoginDetails(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    isactive = models.CharField(max_length=30)
    class Meta:
        db_table = "LOGIN_MASTER"
