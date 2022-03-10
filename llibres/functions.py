import csv
import literals as lit
import datetime

def insert_data():
    video = dict()
    video['identificador'] = int(input(lit.msg1))
    video['grup'] = input(lit.msg2)
    video['canço'] = input(lit.msg3)
    dia=int(input(lit.dies))
    while dia<1 or dia>30:
        dia = int(input(lit.dies))
    mes=int(input(lit.mesos))
    while mes<1 or mes>12:
        mes = int(input(lit.mesos))
    any=int(input(lit.anys))
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    print(date)
    year = date.strftime("%Y")
    year=int(year)
    while any<1970 or any> year:
        any = int(input(lit.anys))
    video['data'] = str(dia)+'/'+str(mes)+'/'+str(any)
    video['nombrevisua'] = int(input(lit.visualitzacions))
    while video['nombrevisua']<1:
        video['nombrevisua'] = int(input(lit.visualitzacions))
    insert_video(video)

def insert_video(video):
    path='files/video.csv'
    header=existint_file(path)

    try:
        with open('files/video.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['identificador', 'grup', 'canço', 'data', 'nombrevisua']
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if header==0:
                    print(lit.crea)
                    writeCSV.writeheader()
            writeCSV.writerow(video)
    except:
        print(lit.noinserir)
    else:
        print(lit.inserir)

def existint_file(path):
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print(lit.noexiste)
        header=0
    else:
         header=1
         f.close()
    finally:
        return header