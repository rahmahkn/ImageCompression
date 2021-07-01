from utils.util import *
from utils.compressSvd import *
from utils.compressHuffman import *

def main():
    showStart()
    showMenu()
    menu = input('\nPilih menu: ')

    while (menu != '3'):
        if (menu == '1'):
            compressImageSVD()
        elif (menu == '2'):
            compressImageHuffman()
        else:
            print("\nNomor menu tidak valid!")

        showMenu()
        menu = input('\nPilih menu: ')

    showExit()

# Main Program
main()