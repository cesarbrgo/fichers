# This is a sample Python scrip

def main ():
    text=input("introdueix un text fins a cen caracters:  ")
    while len(text)>100 or len(text)<1:
        text = input("introdueix un text fins a cen caracters:  ")
    introduce_text(text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
