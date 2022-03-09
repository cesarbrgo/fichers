import csv
def insert_data():
    book = dict()
    book['isbn'] = input("Introdueix l'isbn del llibre: ")
    book['title'] = input("Introdueix el títol del llibre: ")
    book['author'] = input("Introdueix l'autor del llibre: ")
    book['editorial'] = input("Introdueix l'editorial del llibre: ")
    book['pub_date'] = input("Introdueix la data de publicació del llibre: ")
    insert_book(book)

def insert_book(book):
    path='files/books.csv'
    header=existint_file(path)
    with open('files/books.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['isbn', 'title', 'author', 'editorial', 'pub_date']
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        try:
            if header==0:
                writeCSV.writeheader()
            writeCSV.writerow(book)
        except:
            print("No s'ha pogut inserir el registre.")
        else:
            print("El registre s'ha inserit correctament.")

def existint_file(path):
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print("No sha trobat el fitxer")
        header=0
    else:
         header=1
         f.close()
    finally:
        return header


