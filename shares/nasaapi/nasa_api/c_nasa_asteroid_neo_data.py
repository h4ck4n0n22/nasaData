import json
import requests
from datetime import datetime, timedelta
from helpers.c_output_helpers import c_output_helpers
from helpers.c_request_helpers import c_request_helpers

class get_neo_data:
    def __init__(self, out_file, start_date='', end_date=''):
        """ Asteroid near earth object data class init function

        Args:
            out_file (str): name of the file to output the data to
        """
        self.end_date, self.start_date = self.sort_date_ranges(start_date, end_date)
        self.api_key = c_request_helpers.get_api_key()
        self.headers = c_request_helpers.get_request_headers('default')

        json_data = self.get_feed_data()
        c_output_helpers(out_file, 'json', json_data)

    def sort_date_ranges(self, start_date, end_date):
        """ Function to handle date ranges for api request

        Returns:
            str, str: end_date, start_date
            end_date: defaults to today's date
            start_date: defaults to yesterday
        """
        if end_date == '':
            end_date = datetime.now()
        if start_date == '':
            start_date = end_date - timedelta(days=1)
        return(end_date.strftime("%Y-%m-%d"), start_date.strftime("%Y-%m-%d"))
    
    def get_feed_data(self):
        """ Function to obtain asteroid neo data from nasa api

        Args:
            headers (dict): dictionary object containing headers required for get request

        Returns:
            dict: json object return from api request
        """
        get = requests.get(
            f'https://api.nasa.gov/neo/rest/v1/feed?start_date={self.start_date}&end_date={self.end_date}&api_key={self.api_key}',
            headers=self.headers
        )
        json_data = json.loads(get.text)
        return json_data