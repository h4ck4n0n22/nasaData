from helpers.c_nasa_fireball_data import c_nasa_fireball_data

def main():
    with open('art/earth.txt', 'rb') as f:
        for line in f:
            print(line)
        f.close()

if __name__ == '__main__':
    c_nasa_fireball_data('./outputs/fireball.csv')