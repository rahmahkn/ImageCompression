import math, time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy.lib.npyio import save

# Function to convert percentage to number of vectors
def percentToNb(percent, w, h):
    return int(math.ceil((percent * w * h * 0.01) / (w + h + 1)))

# Function to save image with certain name
def saveImage(arr, name):
    filename = '../out/' + name + '_compressed.jpg'

    return Image.fromarray(arr).save(filename)

# Function to convert image to matrix
def imageToMatrix(img):
    sizeX, sizeY = img.size
    arr = np.array(list(img.getdata(band=0)), dtype="uint8")
    arrReshaped = arr.reshape(sizeY, sizeX)
    matrix = np.matrix(arrReshaped)

    return matrix

# Function to compress image from matrix
def constructImage(matrix, nbVector):
    U, sigma, V = np.linalg.svd(matrix)
    compress = np.matrix(U[:, :nbVector]) * np.diag(sigma[:nbVector]) * np.matrix(V[:nbVector, :])

    return compress

# Function to do whole compression until saving the image
def compressImageSVD():
    try:
        imgPath = "r" + input("Input file path: ")
        img = Image.open(imgPath)
        filename = img.filename[:len(filename)-3]
    except:
        print("File path not found!")
        compressImageSVD()
    finally:
        # Getting detail of compression
        percent = int(input("Compress image percentage: "))
        nbVector = percentToNb(percent, img.size[0], img.size[1])

        # Convert image to matrix
        matrix = imageToMatrix(img, nbVector)
        compressedMatrix = constructImage(matrix, nbVector)

        # Saving compressed matrix to new image
        saveImage(compressedMatrix, img.filename)

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
# print(percentToNb(3.2, 3900, 2600))