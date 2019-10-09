import requests
from random import randrange
from datetime import datetime


class TodaysInfo(object):

    @staticmethod
    def get_response(event_type):
        """
        :param event_type: events / deaths / births
        :return:
        """
        date = datetime.today().strftime("%d %m").split(' ')
        day, month = int(date[0]), int(date[1])
        headers = {'accept': 'application/json'}
        try:
            return requests.get(f'https://byabbe.se/on-this-day/{month}/{day}/{event_type}.json',
                                headers=headers)
        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def get_response_data(response, event_type):
        if response.status_code == 200:
            json_response = response.json()
            random_item = randrange(len(json_response[event_type]))
            output = json_response[event_type][random_item]
            return output
        else:
            return None

    def todays_event(self):
        response = self.get_response('events')
        output = self.get_response_data(response, 'events')
        return output

    def todays_deaths(self):
        response = self.get_response('deaths')
        output = self.get_response_data(response, 'deaths')
        return output

    def todays_births(self):
        response = self.get_response('births')
        output = self.get_response_data(response, 'births')
        return output
