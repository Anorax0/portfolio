import logging
from django.db import models
from django.conf import settings
from requests import request

log = logging.getLogger(__name__)


class WeatherAPI(models.Model):
    response = None

    def send_request(self) -> None:
        try:
            self.response = request(
                "GET",
                f"https://weatherdbi.herokuapp.com/data/weather/{settings.LOCATION}",
            ).json()
        except Exception:
            log.error("Cannot retrieve weather data.")

    def get_summary(self) -> str:
        if not self.response:
            return "Service unavailable."
        return self.response["currentConditions"]["comment"]

    def get_temperature(self) -> str:
        if not self.response:
            return "Service unavailable."
        return self.response["currentConditions"]["temp"]["c"]

    def get_humidity(self) -> str:
        if not self.response:
            return "Service unavailable."
        return self.response["currentConditions"]["humidity"]

    def get_wind_speed(self) -> str:
        if not self.response:
            return "Service unavailable."
        return self.response["currentConditions"]["wind"]["km"]

    def get(self) -> dict:
        if not self.response:
            self.send_request()
        output = {
            "forecast_summary": self.get_summary(),
            "forecast_temperature": self.get_temperature(),
            "forecast_humidity": self.get_humidity(),
            "forecast_windspeed": self.get_wind_speed(),
        }
        return output
