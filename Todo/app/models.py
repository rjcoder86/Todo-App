import datetime

import django
from django.db import models

# Create your models here.
class Tasks(models.Model):
    task=models.CharField(max_length=100)
    date=models.DateField(default=datetime.datetime.today)
    is_complete=models.BooleanField(default=False)