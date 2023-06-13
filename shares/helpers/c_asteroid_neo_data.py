import json
import requests
import os
from datetime import datetime, timedelta
from helpers.c_output_helpers import c_output_helpers

output_directory = os.path.join(os.getcwd(), 'outputs')
helpers_directory = os.path.join(os.getcwd(), 'helpers')

class c_asteroid_neo_data:
    def __init__(self, out_file, start_date='', end_date=''):
        """ Asteroid near earth object data class init function

        Args:
            out_file (string): name of the file to output the data to
        """
        self.out_file = f'{output_directory}/{out_file}.json'
        self.end_date, self.start_date = self.sort_date_ranges(start_date, end_date)

        with open(f'{helpers_directory}/keys.json') as api_key_file:
            loaded_data = json.load(api_key_file)
            self.api_key = loaded_data['api_key']

        with open(f'{helpers_directory}/default_headers.json') as headers_config:
            headers = json.load(headers_config)

        json_data = self.get_feed_data(headers)
        c_output_helpers(self.out_file, 'json', json_data)

    def sort_date_ranges(self, start_date, end_date):
        """ Function to handle date ranges for api request

        Returns:
            string, string: end_date, start_date
            end_date: defaults to today's date
            start_date: defaults to yesterday
        """
        if end_date == '':
            end_date = datetime.now()
        if start_date == '':
            start_date = end_date - timedelta(days=1)
        return(end_date.strftime("%Y-%m-%d"), start_date.strftime("%Y-%m-%d"))
    
    def get_feed_data(self, headers):
        """ Function to obtain asteroid neo data from nasa api

        Args:
            headers (dict): dictionary object containing headers required for get request

        Returns:
            dict: json object return from api request
        """
        get = requests.get(
            f'https://api.nasa.gov/neo/rest/v1/feed?start_date={self.start_date}&end_date={self.end_date}&api_key={self.api_key}',
            headers=headers
        )
        json_data = json.loads(get.text)
        return json_data