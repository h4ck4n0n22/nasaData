import os
import json
import csv

output_directory = os.path.join(os.getcwd(), 'outputs')

class c_output_helpers:
    def __init__(self, out_file, filetype, data):
        self.out_file = out_file
        self.filetype = filetype
        self.data = data

        match self.filetype:
            case 'txt':
                self.handle_txt_data()
            case 'json':
                self.handle_json_data()
            case 'csv':
                self.handle_csv_data()
            case _:
                print(self.help_output())
                exit()
    
    def help_output(self):
        """
        """
        help_string = """
        Writing data to file failure

        filetype can be one of:
        * txt
        * json
        * csv
        """
        return help_string
    
    def handle_txt_data():
         pass
    
    def handle_json_data(self):
        """ helper function to dave json data to disk
        """
        json_object = json.dumps(self.data, indent=4)
        with open(f'{output_directory}/{self.out_file}.json', mode = 'w') as data_file:
            data_file.write(json_object)
    
    def handle_csv_data(self):
        """ Helper function to save csv data to disk
        """
        with open(f'{output_directory}/{self.out_file}.csv',
                  mode = 'w', newline = '') as data_file:
            data_writer = csv.writer(
                data_file,
                delimiter = ',',
                quotechar = '"',
                quoting = csv.QUOTE_ALL
            )

            field_names = self.data['fields']
            data_writer.writerow(field_names)

            for record in self.data['data']:
                data_writer.writerow(record)
    
    