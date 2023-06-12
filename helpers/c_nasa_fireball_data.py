import requests
import json
import csv

class c_nasa_fireball_data:
    """ NASA Fireball Data Class
    """
    def __init__(self, out_file):
        """ Fireball data class init function

        Args:
            out_file (string): name of file to write data to
        """
        self.out_file = out_file
        headers = {
            'Content-type': 'application/json'
        }
        json_data = self.get_data(headers)
        
        self.write_data_to_csv(json_data)
    
    def get_data(self, headers):
        """ Function to collect fireball api data

        Args:
            headers (dict): http headers for post request

        Returns:
            dict: json object containing requests response
        """
        post = requests.post('https://ssd-api.jpl.nasa.gov/fireball.api', headers = headers)
        json_data = json.loads(post.text)
        return json_data

    def write_data_to_csv(self, json_data):
        """ Function to pull out json data and populate into a csv file

        Args:
            json_data (dict): returned json object containing fireball api data
        """
        with open(self.out_file, mode = 'w', newline = '') as data_file:
            data_writer = csv.writer(
                data_file,
                delimiter = ',',
                quotechar = '"',
                quoting = csv.QUOTE_ALL
            )

            field_names = json_data['fields']
            data_writer.writerow(field_names)

            for record in json_data['data']:
                data_writer.writerow(record)