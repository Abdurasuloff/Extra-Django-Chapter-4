from django.db import models
from django.utils.timezone import datetime

# Create your models here.


class Notification(models.Model):
    body = models.CharField(max_length=250)
    datetime = models.DateTimeField(default=datetime.now())
    sent = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body