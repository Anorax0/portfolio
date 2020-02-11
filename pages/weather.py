from django.db import models
from django.utils.timezone import now
from darksky.api import DarkSky
from darksky.types import languages, units, weather
from portfolio.settings import DARKSKY_API_KEY


class DarkSkyApi(models.Model):
    forecast_summary = models.CharField(max_length=1000)
    forecast_temperature = models.FloatField()
    forecast_humidity = models.FloatField()
    forecast_windspeed = models.FloatField()
    forecast_pressure = models.FloatField()
    forecast_date = models.DateTimeField(default=now)

    # init with API key
    darksky = DarkSky(DARKSKY_API_KEY)

    # set location to Gdynia, pomorskie, Poland
    latitude = 54.5432
    longitude = 18.4992

    class Meta:
        verbose_name = "Weather Data"
        verbose_name_plural = "Weather Data"

    def get(self):
        return self.get_weather_data()

    def get_data_from_database(self):
        pass

    def put_data_to_database(self):
        pass

    def get_weather_data(self):
        forecast = self.darksky.get_forecast(
            self.latitude, self.longitude,
            extend=False,  # default `False`
            lang=languages.ENGLISH,  # default `ENGLISH`
            units=units.AUTO,  # default `auto`
            exclude=[weather.MINUTELY, weather.ALERTS]  # default `[]`
        )
        return forecast
