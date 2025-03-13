from django.db import models

# Create your models here.

class Task(models.Model):
    task_date=models.DateField()
    title=models.CharField(max_length=100)
    assigned=models.CharField(max_length=100)
    due_date=models.DateField()
    check_box=models.BooleanField(default=False)
   