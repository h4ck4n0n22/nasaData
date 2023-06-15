import requests
import json
from helpers.c_output_helpers import c_output_helpers
from helpers.c_request_helpers import c_request_helpers

class get_fireball_data:
    """ NASA Fireball Data Class
    """
    def __init__(self, out_file):
        """ Fireball data class init function

        Args:
            out_file (str): name of file to write data to
        """
        self.headers = c_request_helpers.get_request_headers('default')
        json_data = self.get_data()
        
        c_output_helpers(out_file, 'csv', json_data)
    
    def get_data(self):
        """ Function to collect fireball api data

        Returns:
            dict: json object containing requests response
        """
        post = requests.post(
            'https://ssd-api.jpl.nasa.gov/fireball.api',
            headers = self.headers
        )
        
        json_data = json.loads(post.text)
        return json_data