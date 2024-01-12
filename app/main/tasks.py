from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings
from .models import Notification

from channels.layers import get_channel_layer
import asyncio
import json


@shared_task
def send_mail_task(subject, message, recipient_list):
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        return "Jo'natildi."
    except:
        return "Jo'natib bo'lmadi"
    
    
@shared_task
def slow_func():
    for i in range(30000):
        print(i)
        

@shared_task       
def send_notification(notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        channel_layer = get_channel_layer()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            channel_layer.group_send(
                "notification_room",
                {"type":"send_notification", "message":json.dumps(notification.body)}
            )
        )
        notification.sent = True
        notification.save()
        return "Ok"
    except:
        return "Error!"
        