import timeit, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path

# Function to save image with certain name
def saveImageSvd(arr, name):
    filename = '..\\out\\' + name + '_svd.jpg'
    img = Image.fromarray(arr).convert('RGB').save(filename)

    return filename

# Function to convert image to matrix
def imageToMatrix(img):
    sizeX, sizeY = img.size
    arr = np.array(list(img.getdata(band=0)), dtype="uint8")
    print(len(arr))
    arrReshaped = arr.reshape(sizeY, sizeX)
    matrix = np.matrix(arrReshaped)

    return matrix

# Function to compress image from matrix
def constructImage(matrix, nbVector):
    U, sigma, V = np.linalg.svd(matrix)
    compress = np.matrix(U[:, :nbVector]) * np.diag(sigma[:nbVector]) * np.matrix(V[:nbVector, :])

    return compress

# Function to do whole svd compression until saving the image
def compressImageSVD():
    try:
        # Getting file path
        imgPath = input("Input file path: ")

        startTime = timeit.default_timer()
        startSize = os.stat(imgPath).st_size

        img = Image.open(imgPath)
        filename = Path(imgPath).stem

        # Getting filename
        # list_filename = (img.filename[:len(img.filename)-4]).split('\\')
        # filename = list_filename.pop()
        # print(filename)
    except:
        print("File path not found!")
        compressImageSVD()
    finally:
        # Getting detail of compression
        print("\nYou can have a compression rate between 1-" + str(min(img.size)))
        percent = int(input("Compression rate: "))

        # Convert image to matrix
        matrix = imageToMatrix(img)
        compressedMatrix = constructImage(matrix, percent)

        # Saving compressed matrix to new image
        savedImage = saveImageSvd(compressedMatrix, filename)

        # Getting runtime and compression percentage
        endTime = timeit.default_timer()
        endSize = os.stat(savedImage).st_size

        print('\nRuntime program: ' + str(endTime - startTime) + " s")
        print('Compression percentage: ' + str(endSize * 100 /startSize) + " %")

# Function to show start display
def showStart():
    print(
        '''                                       
                _                                           
                |_|_____ ___ ___ ___                         
                | |     | .'| . | -_|                        
                |_|_|_|_|__,|_  |___|                        
                            |___|                                                    
                                        _         
        ___ ___ _____ ___ ___ ___ ___ ___|_|___ ___ 
        |  _| . |     | . |  _| -_|_ -|_ -| | . |   |
        |___|___|_|_|_|  _|_| |___|___|___|_|___|_|_|
                    |_|                            
        '''
    )

# Function to show menu
def showMenu():
    print(
        '''
1. Compress image with SVD
2. Compress image with Huffman Coding
3. Exit
        '''
    )

# Function to show exit display
def showExit():
    print('\nSee you next time!')

# print(percentToNb(3.2, 3900, 2600))