import requests
import json
from datetime import datetime, timedelta
from helpers.c_request_helpers import c_request_helpers
from helpers.c_output_helpers import c_output_helpers
from nasa_api import c_nasa_donki_data

class get_donki_data:
    def __init__(self, donki_type, out_file, start_date='', end_date=''):
        """_summary_

        Args:
            donki_type (str): one of 
                cme, cmea, gst, ips, flr, sep, mpc, rbe, hss, wsa, notifications.
            out_file (str): name of file to write data to
            start_date (str, optional): start of date range for request. Defaults to ''.
            end_date (str, optional): end of date range for request. Defaults to ''.
        """
        try:
            self.headers = c_request_helpers.get_request_headers('default')

            self.base_url, self.base_url_end = self.handle_request_baselines(
                start_date, end_date)
            match donki_type:
                case 'cme':
                    json_data = self.get_cme_data()
                case 'cmea':
                    json_data = self.get_cmea_data()
                case 'gst':
                    json_data = self.get_gst_data()
                case 'ips':
                    json_data = self.get_ips_data()
                case 'flr':
                    json_data = self.get_flr_data()
                case 'sep':
                    json_data = self.get_sep_data()
                case 'mpc':
                    json_data = self.get_mpc_data()
                case 'rbe':
                    json_data = self.get_rbe_data()
                case 'hss':
                    json_data = self.get_hss_data()
                case 'wsa':
                    json_data = self.get_wsa_data()
                case 'notifications':
                    json_data = self.get_notifications_data()
                case _:
                    pass

            c_output_helpers(out_file, 'json', json_data)
        except json.JSONDecodeError as json_err:
            print(json_err)
            c_nasa_donki_data.get_donki_data(donki_type,
                                             out_file, 
                                             '2016-01-01', 
                                             '2016-01-30')
    
    def handle_request_baselines(self, start_date, end_date):
        """ Function to handle baseline url generation

        Args:
            start_date (str, optional): start of date range for request. Defaults to ''.
            end_date (str, optional): end of date range for request. Defaults to ''.
        """
        api_key = c_request_helpers.get_api_key()
        if start_date == '' and end_date == '':
            end_date, start_date = self.sort_date_ranges()

        base_url = 'https://api.nasa.gov/DONKI'
        base_url_end = f'startDate={start_date}&endDate={end_date}&api_key={api_key}'  # noqa: E501

        return base_url, base_url_end
    
    def sort_date_ranges(self):
        """ Function to handle date ranges for api request

        Returns:
            str, str: end_date, start_date
            end_date: defaults to today's date
            start_date: defaults to 30 days ago
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        return(end_date.strftime("%Y-%m-%d"), start_date.strftime("%Y-%m-%d"))
    
    def get_cme_data(self):
        """ Coronal Mass Ejection Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/CME?{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_cmea_data(self):
        """ Coronal Mass Ejection Analysis Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/CMEAnalysis?mostAccurateOnly=true&speed=500&halfAngle=30&catalog=ALL&{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_gst_data(self):
        """ Geomagnetic Storm Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/GST?{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_ips_data(self):
        """ Interplanetary Shock Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/IPS?location=ALL&catalog=ALL&{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_flr_data(self):
        """ Solar Flare Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/FLR?{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_sep_data(self):
        """ Solar Energetic Particle Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/SEP?{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_mpc_data(self):
        """ Magnetopause Crossing Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/MPC?{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_rbe_data(self):
        """ Radiation Belt Enhancement Data

        Returns:
           dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/RBE?{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_hss_data(self):
        """ Hight Speed Stream Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/HSS?{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_wsa_data(self):
        """ WSA+EnlilSimulation Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/WSAEnlilSimulations?{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)
    
    def get_notifications_data(self):
        """ Notifications Data

        Returns:
            dict: json return from api request
        """
        get = requests.get(
            f'{self.base_url}/notifications?type=all&{self.base_url_end}',
            headers=self.headers
        )
        return json.loads(get.text)