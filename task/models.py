from django.db import models

# Create your models here.

class Product(models.Model):
    check_box=models.BooleanField(default=False)
    title=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
   