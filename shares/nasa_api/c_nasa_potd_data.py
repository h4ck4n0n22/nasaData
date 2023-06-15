import requests
import json
from helpers.c_output_helpers import c_output_helpers
from helpers.c_request_helpers import c_request_helpers

class get_potd_data:
    """ NASA Astronomy Picture of the Day Class
    """
    def __init__(self, out_file):
        """ PotD data class init function

        Args:
            out_file (str): name of file to write data to
        """
        self.api_key = c_request_helpers.get_api_key()
        self.headers = c_request_helpers.get_request_headers('default')

        json_data = self.get_data()
        
        c_output_helpers(out_file, 'json', json_data)
    
    def get_data(self):
        """ Function to collect fireball api data

        Args:
            headers (dict): http headers for post request

        Returns:
            dict: json object containing requests response
        """
        get = requests.get(
            f'https://api.nasa.gov/planetary/apod?api_key={self.api_key}',
            headers = self.headers
        )
        
        json_data = json.loads(get.text)
        return json_data