from utils.util import *
from utils.compressSvd import *
from utils.compressHuffman import *

def main():
    showStart()
    showMenu()
    menu = int(input('\nPilih menu: '))

    while (menu != 3):
        if (menu == 1):
            compressImageSVD()
        elif (menu == 2):
            compressImageHuffman()
        else:
            print("Nomor menu tidak valid!")

        showMenu()
        menu = int(input('\nPilih menu: '))

# Main Program
main()