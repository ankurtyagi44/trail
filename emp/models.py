from django.db import models

# Create your models here.
class EMP(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=10)
    phone_no=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    dept=models.CharField(max_length=10)
    working=models.BooleanField(default=True)

