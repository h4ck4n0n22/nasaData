import sys
import getopt
from helpers.c_nasa_fireball_data import c_nasa_fireball_data
from helpers.c_asteroid_neo_data import c_asteroid_neo_data

def help_output():
    help_string = """
    main.py -d <datatype> -o <outfile>

    datatype can be one of:
    * fireball
    * asteroid_neo
    """
    return help_string

def select_data(datatype, outfile):
    match datatype:
        case 'fireball':
            c_nasa_fireball_data(outfile)
        case 'asteroid_neo':
            c_asteroid_neo_data(outfile)
        case _:
            print(help_output())
            exit()

def main(argv):
    datatype = ''
    outfile = ''
    try:
        opts, args = getopt.getopt(argv,"hd:o:",["datatype=","outfile="])
    except getopt.GetoptError:
        print(help_output())
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print(help_output())
            sys.exit()
        elif opt in ('-d', '--datatype'):
            datatype = arg
        elif opt in ('-o', '--outfile'):
            outfile = arg
    
    select_data(datatype, outfile)

if __name__ == '__main__':
    main(sys.argv[1:])