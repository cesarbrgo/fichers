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