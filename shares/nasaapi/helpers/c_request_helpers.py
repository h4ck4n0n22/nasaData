import os
import json

helpers_directory = os.path.join(os.getcwd(), 'helpers')

class c_request_helpers:

    def get_api_key():
        """ Helper function to load in API key

        Returns:
            str: api key value
        """
        with open(f'{helpers_directory}/keys.json') as api_key_file:
            loaded_data = json.load(api_key_file)
            api_key = loaded_data['api_key']
        return api_key

    def get_request_headers(type):
        """ Helper function to read in headers object

        Returns:
            dict: headers object for requests
        """
        with open(f'{helpers_directory}/{type}_headers.json') as headers_config:
            headers = json.load(headers_config)
        return headers