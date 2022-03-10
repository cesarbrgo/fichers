import csv
import literals as lit
import datetime

def get_info():
        line_count=0
        total_woman=0
        with open('files/Creus.csv') as csvfile:
            readCSV=csv.DictReader(csvfile)
            for row in readCSV:
                if row['Sexe']=='Dona':
                    total_woman+=1
                line_count+=1
        print("el total de dones es:", total_woman, 'el total de registres es: ', line_count)