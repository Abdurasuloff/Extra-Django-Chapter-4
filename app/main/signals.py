from .models import Notification
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_celery_beat.models import ClockedSchedule, PeriodicTask
from uuid import uuid4
import json



@receiver(post_save, sender=Notification)
def send_notificiation_after_model_creation(instance, created, *args, **kwargs):
    if created:
        clocked = ClockedSchedule.objects.create(clocked_time=instance.datetime)
        
        task = PeriodicTask.objects.create(
            name = f"{instance.body}-{uuid4()}",
            clocked = clocked,
            task = "main.tasks.send_notification",
            one_off=True, 
            kwargs=json.dumps({"notification_id":instance.id})
        )
        
        print(instance.body)
        