from django.db import models

# Create your models here.
developer=[
        ("Anuj" ,"Anuj"),
        ("Sourav" ,"Sourav"),
        ]
class Todo(models.Model):
    start_date=models.DateField()
    title=models.CharField(max_length=100)
    assigned=models.CharField(max_length=100,choices=developer,blank=True)
    end_date=models.DateField()
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='1. Todo'