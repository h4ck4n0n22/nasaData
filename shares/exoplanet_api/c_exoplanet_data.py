import json
import requests
from helpers.c_output_helpers import c_output_helpers
from helpers.c_request_helpers import c_request_helpers

class get_exoplanet_data:
    def __init__(self, exo_data_type, out_file):
        try:
            self.base_url = self.handle_request_baselines()
            self.headers = c_request_helpers.get_request_headers('default')
            match exo_data_type:
                case 'kooi':
                    json_data = self.get_kepler_objects_of_interest()
                case 'tce':
                    json_data = self.get_threshold_crossing_events()
                case 'kst':
                    json_data = self.get_kepler_stellar_table()
                case 'k2t':
                    json_data = self.get_k2_targets()
                case 'maes':
                    json_data = self.get_mission_and_exocat_stars()
                case 'cpm':
                    json_data = self.get_confirmed_planets_microlensing()
                case _:
                    pass
            c_output_helpers(out_file, 'json', json_data)
        except json.JSONDecodeError as json_err:
            print(json_err)
            exit(1)

    def handle_request_baselines(self):
        base_url = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?'
        return base_url

    def get_kepler_objects_of_interest(self):
        get = requests.get(
            f'{self.base_url}table=cumulative&format=json',
            headers = self.headers
        )
        return json.loads(get.text)

    def get_threshold_crossing_events(self):
        get = requests.get(
            f'{self.base_url}table=q1_q17_dr25_tce&format=json',
            headers = self.headers
        )
        return json.loads(get.text)

    def get_kepler_stellar_table(self):
        get = requests.get(
            f'{self.base_url}table=keplerstellar&format=json',
            headers = self.headers
        )
        return json.loads(get.text)

    def get_k2_targets(self):
        get = requests.get(
            f'{self.base_url}table=k2targets&format=json',
            headers = self.headers
        )
        return json.loads(get.text)

    def get_mission_and_exocat_stars(self):
        get = requests.get(
            f'{self.base_url}table=mission_exocat&format=json',
            headers = self.headers
        )
        return json.loads(get.text)

    def get_confirmed_planets_microlensing(self):
        get = requests.get(
            f'{self.base_url}table=ML&format=json',
            headers = self.headers
        )
        return json.loads(get.text)