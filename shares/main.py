import sys
import getopt
from nasa_api import c_nasa_fireball_data, c_nasa_asteroid_neo_data, c_nasa_potd_data, c_nasa_donki_data
from exoplanet_api import c_exoplanet_data

def help_output():
    help_string = """
    main.py -d <datatype> -o <out_file> [optional: -k <donki_type>]

    datatype can be one of:
    * fireball
    * asteroid_neo
    * potd
    * donki [must include donki_type (-k)] one of:
        - cme
        - cmea
        - gst
        - ips
        - flr
        - sep
        - mpc
        - rbe
        - hss
        - wsa
        - notifications
    * exoplanet [must include exo_data_type (-e)] one of:
        - kooi
        - tce
        - kst
        - k2t
        - maes
        - cpm
    """
    return help_string

def select_data(datatype, out_file, donki_type='', exo_data_type=''):
    """_summary_

    Args:
        datatype (_type_): _description_
        out_file (_type_): _description_
        donki_type (str, optional): _description_. Defaults to ''.
    """
    match datatype:
        case 'fireball':
            c_nasa_fireball_data.get_fireball_data(out_file)
        case 'asteroid_neo':
            c_nasa_asteroid_neo_data.get_neo_data(out_file)
        case 'potd':
            c_nasa_potd_data.get_potd_data(out_file)
        case 'donki':
            if donki_type == '':
                print(help_output())
                exit()
            c_nasa_donki_data.get_donki_data(donki_type, out_file)
        case 'exoplanet':
            if exo_data_type == '':
                print(help_output())
                exit()
            c_exoplanet_data.get_exoplanet_data(exo_data_type, out_file)
        case _:
            print(help_output())
            exit()

def main(argv):
    datatype = ''
    out_file = ''
    donki_type = ''
    exo_data_type = ''
    try:
        opts, args = getopt.getopt(argv,"hd:o:k:e:",
                                   ["datatype=",
                                    "out_file=",
                                    "donki_type=",
                                    "exo_data_type="]
                                )
    except getopt.GetoptError:
        print(help_output())
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print(help_output())
            sys.exit()
        elif opt in ('-d', '--datatype'):
            datatype = arg
        elif opt in ('-o', '--out_file'):
            out_file = arg
        elif opt in ('-k', '--donki_type'):
            donki_type = arg
        elif opt in ('-e', '--exo_data_type'):
            exo_data_type = arg
    
    select_data(datatype, out_file, donki_type, exo_data_type)

if __name__ == '__main__':
    main(sys.argv[1:])