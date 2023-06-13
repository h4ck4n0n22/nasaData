import requests
import json
from helpers.c_output_helpers import c_output_helpers

class c_nasa_fireball_data:
    """ NASA Fireball Data Class
    """
    def __init__(self, out_file):
        """ Fireball data class init function

        Args:
            out_file (string): name of file to write data to
        """
        self.out_file = f'outputs/{out_file}.csv'
        headers = {
            'Content-type': 'application/json'
        }
        json_data = self.get_data(headers)
        
        c_output_helpers(self.out_file, 'csv', json_data)
    
    def get_data(self, headers):
        """ Function to collect fireball api data

        Args:
            headers (dict): http headers for post request

        Returns:
            dict: json object containing requests response
        """
        post = requests.post(
            'https://ssd-api.jpl.nasa.gov/fireball.api',
            headers = headers
        )
        
        json_data = json.loads(post.text)
        return json_data