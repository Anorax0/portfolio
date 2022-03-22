import requests
from random import randint
from datetime import datetime
import logging

log = logging.getLogger(__name__)


class TodaysInfo:
    response = {"events": {}, "deaths": {}, "births": {}}

    def get_response(self, event_type: str) -> None:
        """
        :param event_type: events / deaths / births
        :return: None
        """
        date = datetime.today().strftime("%d %m").split(" ")
        day, month = int(date[0]), int(date[1])
        headers = {"accept": "application/json"}
        try:
            self.response[event_type] = requests.request(
                "GET",
                f"https://byabbe.se/on-this-day/{month}/{day}/{event_type}.json",
                headers=headers,
            ).json()
        except requests.exceptions.RequestException as e:
            log.error("Cannot retrieve today's info due to error: ", e)

    def get_response_data(self, event_type: str) -> str:
        random_item = randint(0, len(self.response.get(event_type)[event_type]) - 1)
        output = self.response.get(event_type)[event_type][random_item]
        return output

    def todays_event(self):
        return self.get_response_data("events")

    def todays_deaths(self):
        return self.get_response_data("deaths")

    def todays_births(self):
        return self.get_response_data("births")

    def get_events(self):
        self.get_response("events")
        self.get_response("deaths")
        self.get_response("births")

        return {
            "events": self.todays_event(),
            "deaths": self.todays_deaths(),
            "births": self.todays_births(),
        }
