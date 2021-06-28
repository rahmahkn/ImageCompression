from PIL import Image
from pathlib import Path
import numpy as np
import os, timeit

# Function to convert image to pixels
def imageToPixels(img):
    sizeX, sizeY = img.size
    arr = np.array(list(img.getdata(band=0)), dtype="uint8")
    arrReshaped = arr.reshape(sizeY, sizeX)
    matrix = np.matrix(arrReshaped)

    return matrix

# Function to encode pixels into huffman code

# Function to decode huffman code into pixels

# Function to create image from pixels
def pixelsToImage(pixels, name):
    array = np.random.random_integers(0, 255, (500, 500, 3))
    array = np.array(array, dtype=np.uint8)
    img = Image.fromarray(pixels)

    filename = '..\\out\\' + name + '_huffman.jpg'
    img.save(filename)

    return filename

# Function to do whole huffman compression until saving the image
def compressImageHuffman():
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
        compressImageHuffman()
    finally:
        # Convert image to pixels
        matrix = imageToPixels(img)

        # Convert matrix of pixels to image and save it
        savedImage = pixelsToImage(matrix, filename)

        # Getting runtime and compression percentage
        endTime = timeit.default_timer()
        endSize = os.stat(savedImage).st_size

        print('\nRuntime program: ' + str(endTime - startTime) + " s")
        print('Compression percentage: ' + str(endSize * 100 /startSize) + " %")        

# pixelsToImage([], "test")    