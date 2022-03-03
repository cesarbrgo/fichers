# This is a sample Python scrip
import functions as func
import literals as lite
def main ():
    print(lite.menu)
    print(lite.opcio1)
    ele=int(input(lite.opcio2))
    cont=0
    match ele:
        case 1:
                contador = 0
                func.introduce_name(contador)
        case 2:
                contador=0
                func.write_csv(contador)
        case _:
                print("error")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
