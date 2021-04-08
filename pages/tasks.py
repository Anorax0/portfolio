from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail


@shared_task()
def send_email_task(name):
    send_mail(f'You have new message from {name}',
              'Please check admin site to see unreaded messages -> http://https://anorax.herokuapp.com/',
              settings.EMAIL_HOST_USER,
              [settings.EMAIL_RECEIVER])
    return None
