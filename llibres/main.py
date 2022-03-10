import csv
import functions as fun

def main():
        stop = 1
        while stop != 0:
            fun.insert_data()
            stop = int(input("vols parar d'introduir registres? introdueix 0: "))

if __name__ == '__main__':
    main()