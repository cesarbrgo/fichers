import literals as lite
import csv

def crea_arxiu(text):
    try:
        f = open("files/text.txt", "w+")
    except:
        print("error")
    else:
        f.write(text)
        f.close()

def introduce_text(text):
    try:
        f = open("files/text.txt", "a+")
    except:
        print("error")
    else:
        f.write(text)
        f.close()

def introduce_name(contador):
    try:
        nom = input(lite.introdueix)
        with open('files/'+nom+'.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                print(f'\t Estudiant:{row[0]}, {row[1]} {row[2]}, a la matèria {row[3]} ha obtingut un {row[4]}.')
    except FileNotFoundError:
        print("No sha trobat el fitxer")
        contador=contador+1
        print(contador)
        if contador<=3:
            introduce_name(contador)
        else:
            print("error")
    else:

        print("Tot va bé")
    finally:
        print("Final del programa")
def write_csv(contador):
    try:
        nom = input(lite.introdueix)

        with open('files/'+nom+'.csv', 'a') as csvfile:
            writeCSV = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            text=input(lite.introdueix_text)
            writeCSV.writerow(text)
    except FileNotFoundError:
        print("No sha trobat el fitxer")
        contador=contador+1
        print(contador)
        if contador<=3:
            introduce_name(contador)
        else:
            print("error")
    else:
        print("Tot va bé")