from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail

from .weather import DarkSkyApi


@shared_task()
def send_email_task(name):
    send_mail(f'You have new messege from {name}',
              'Please check admin site to see unreaded messeges -> http://https://anorax.herokuapp.com/',
              settings.EMAIL_HOST_USER,
              [settings.EMAIL_RECEIVER])
    return None


@shared_task()
def get_weather_task():
    weather = DarkSkyApi().get()
    qs = DarkSkyApi(forecast_summary=weather.currently.summary,
                    forecast_temperature=weather.currently.temperature,
                    forecast_humidity=weather.currently.humidity,
                    forecast_windspeed=weather.currently.wind_speed,
                    forecast_pressure=weather.currently.pressure)
    qs.save()
    return qs
