from PIL import Image
from pathlib import Path
import numpy as np
import os, timeit, queue, imageio
from scipy.misc import *

# Class Node to build the tree
class Node:
	def __init__(self):
		self.prob = None
		self.code = None
		self.data = None
		self.left = None
		self.right = None

	def __lt__(self, other):
		if (self.prob < other.prob):
			return 1
		else:
			return 0

	def __ge__(self, other):
		if (self.prob > other.prob):
			return 1
		else:
			return 0

# Function to make huffman tree
def tree(probabilities):
    prq = queue.PriorityQueue()
    for color,probability in enumerate(probabilities):
        leaf = Node()
        leaf.data = color
        leaf.prob = probability
        prq.put(leaf)

    while (prq.qsize()>1):
        # Creating new node
        newnode = Node()

        # Get the smallest probs in the leaves
        l = prq.get()
        r = prq.get()		
        
        # Remove the smallest two leaves and make new node inserted in leaf
        newnode.left = l # left is smaller
        newnode.right = r
        newprob = l.prob + r.prob
        newnode.prob = newprob
        prq.put(newnode)

    return prq.get()

# Function to do traversal of the tree to generate codes
def huffmanTraversal(rootNode, tempArray, huffmanCode):
    if (rootNode.left is not None):
        tempArray[huffmanTraversal.count] = 1
        huffmanTraversal.count += 1
        huffmanTraversal(rootNode.left,tempArray,huffmanCode)
        huffmanTraversal.count -= 1

    if (rootNode.right is not None):
        tempArray[huffmanTraversal.count] = 0
        huffmanTraversal.count += 1
        huffmanTraversal(rootNode.right,tempArray,huffmanCode)
        huffmanTraversal.count -= 1
    else:
        # Count the number of bits for each color
        huffmanTraversal.output_bits[rootNode.data] = huffmanTraversal.count
        bitstream = ''.join(str(cell) for cell in tempArray[1:huffmanTraversal.count]) 
        color = str(rootNode.data)
        huffmanCode[color] = bitstream

    return

# Function to change image pixels into grayscale
def rgbToGray(img):
    grayImg = np.rint(img[:,:,0]*0.2989 + img[:,:,1]*0.5870 + img[:,:,2]*0.1140)
    grayImg = grayImg.astype('uint8')

    return grayImg

# Function to encode pixels into huffman code
def pixelsToCode(pixels, huffmanCodes, filename):
    f = open(filename, 'w')

    for row in pixels:
        for elmt in row:
            f.write(huffmanCodes[str(elmt)])
            f.write("-")
        f.write("\n")

# Function to decode huffman code into pixels
def codeToPixels(huffmanCodes, filename):
    pixels = []

    f = open(filename)
    for line in f:
        line = line.rstrip()
        tempPixels = []

        bits = line.split("-")

        for bit in bits:
            # Searching pixel number from bit
            key = getKey(huffmanCodes, bit)

            if key != None:
                tempPixels += [int(key)]

        pixels += [tempPixels]

    return pixels

# Function to create image from pixels
def pixelsToImage(pixels, name):
    pixels = np.array(pixels, dtype="uint8")
    img = Image.fromarray(pixels).convert('L')

    filename = '..\\out\\' + name + '_huffman.jpg'
    img.save(filename)

    return filename

# Function to check if code is available in huffman code
def isCodeAvailable(huffmanCodes, code):
    for value in huffmanCodes.values():
        if code in value:
            return True
    
    return False

# Function to get key from value
def getKey(huffmanCodes, value):
    for key, val in huffmanCodes.items():
        if val == value:
            return key

    return None

# Function to do whole huffman compression until saving the image
def compressImageHuffman():
    try:
        # Getting file path
        imgPath = input("Input file path: ")

        startTime = timeit.default_timer()
        startSize = os.stat(imgPath).st_size

        # Getting filename
        filename = Path(imgPath).stem
    except:
        print("File path not found!")
        compressImageHuffman()
    finally:
        img = imageio.imread(imgPath)
        grayImg = rgbToGray(img)

        # Compute histogram of pixels
        hist = np.bincount(grayImg.ravel(), minlength=256)

        # Create probabilities for each pixel number
        probabilities = hist/np.sum(hist)

        # Make the tree based on probabilities
        rootNode = tree(probabilities)
        tempArray = np.ones([64], dtype=int)
        huffmanTraversal.output_bits = np.empty(256, dtype=int) 
        huffmanTraversal.count = 0

        # Getting huffman codes for each pixel number
        huffmanCode = {}
        huffmanTraversal(rootNode,tempArray,huffmanCode)

        # Making txt file that save encode precessed picture
        pixelsToCode(grayImg, huffmanCode, "codes.txt")

        # Decode huffman codes from txt file to array of pixels
        pixels = codeToPixels(huffmanCode, "codes.txt")

        # Convert array of pixels to image and save it
        savedImage = pixelsToImage(pixels, filename)

        # Getting runtime and compression percentage
        endTime = timeit.default_timer()
        endSize = os.stat(savedImage).st_size

        print('\nRuntime program: ' + str(endTime - startTime) + " s")
        print('Compression percentage: ' + str(endSize * 100 /startSize) + " %")   