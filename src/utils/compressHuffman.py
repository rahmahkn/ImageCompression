from PIL import Image
from pathlib import Path
import numpy as np
import os, timeit, queue, imageio
from scipy.misc import *


# Class node to build the tree
class Node:
	def __init__(self):
		self.prob = None
		self.code = None
		self.data = None
		self.left = None
		self.right = None 	# the color (the bin value) is only required in the leaves
	def __lt__(self, other):
		if (self.prob < other.prob):		# define rich comparison methods for sorting in the priority queue
			return 1
		else:
			return 0
	def __ge__(self, other):
		if (self.prob > other.prob):
			return 1
		else:
			return 0

def rgbToGray(img):
    gray_img = np.rint(img[:,:,0]*0.2989 + img[:,:,1]*0.5870 + img[:,:,2]*0.1140)
    gray_img = gray_img.astype(int)
    return gray_img

def getTwoSmallest(data):			# can be used instead of inbuilt function get(). was not used in  implementation
    first = second = 1;
    fid=sid=0
    for idx,element in enumerate(data):
        if (element < first):
            second = first
            sid = fid
            first = element
            fid = idx
        elif (element < second and element != first):
            second = element
    return fid,first,sid,second

def tree(probabilities):
    prq = queue.PriorityQueue()
    for color,probability in enumerate(probabilities):
        leaf = Node()
        leaf.data = color
        leaf.prob = probability
        prq.put(leaf)

    while (prq.qsize()>1):
        newnode = Node()		# create new node
        l = prq.get()
        r = prq.get()			# get the smalles probs in the leaves
                        # remove the smallest two leaves
        newnode.left = l 		# left is smaller
        newnode.right = r
        newprob = l.prob+r.prob	# the new prob in the new node must be the sum of the other two
        newnode.prob = newprob
        prq.put(newnode)	# new node is inserted as a leaf, replacing the other two 
    return prq.get()		# return the root node - tree is complete

def huffman_traversal(root_node,tmp_array,huffmanCode):		# traversal of the tree to generate codes
    if (root_node.left is not None):
        tmp_array[huffman_traversal.count] = 1
        huffman_traversal.count += 1
        huffman_traversal(root_node.left,tmp_array,huffmanCode)
        huffman_traversal.count -= 1

    if (root_node.right is not None):
        tmp_array[huffman_traversal.count] = 0
        huffman_traversal.count += 1
        huffman_traversal(root_node.right,tmp_array,huffmanCode)
        huffman_traversal.count -= 1
    else:
        huffman_traversal.output_bits[root_node.data] = huffman_traversal.count		#count the number of bits for each color
        bitstream = ''.join(str(cell) for cell in tmp_array[1:huffman_traversal.count]) 
        color = str(root_node.data)
        huffmanCode[color] = bitstream
    return

# Function to convert image to pixels
def imageToPixels(img):
    sizeX, sizeY = img.size
    arr = np.array(list(img.getdata(band=0)), dtype="uint8")
    arrReshaped = arr.reshape(sizeY, sizeX)
    matrix = np.matrix(arrReshaped)

    return matrix

# Function to encode pixels into huffman code
def pixelsToCode(pixels, huffmanCodes, filename):
    f = open(filename, 'w')

    for elmt in pixels:
        f.write(huffmanCodes[str(elmt)])

# Function to decode huffman code into pixels
def codeToPixels(huffmanCodes, filename):
    pixels = []

    f = open(filename)
    for line in f:
        temp = []
        for char in f:
            # if temp 

            found = True

            

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

        # startTime = timeit.default_timer()
        # startSize = os.stat(imgPath).st_size

        # # Getting filename
        # filename = Path(imgPath).stem
    except:
        print("File path not found!")
        compressImageHuffman()
    finally:
        img = imageio.imread(imgPath)
        gray_img = rgbToGray(img)

        # Compute histogram of pixels
        hist = np.bincount(gray_img.ravel(),minlength=256)

        # Create probabilities for each pixel number
        probabilities = hist/np.sum(hist)

        # Make the tree using probabilities
        root_node = tree(probabilities)
        tmp_array = np.ones([64],dtype=int)
        huffman_traversal.output_bits = np.empty(256,dtype=int) 
        huffman_traversal.count = 0

        # Getting huffman codes for each pixel number
        huffmanCode = {}
        huffman_traversal(root_node,tmp_array,huffmanCode)		# traverse the tree and write the codes

        # Making txt file that save encode precessed picture
        pixelsToCode(tmp_array, huffmanCode, "codes.txt")

        # Decode huffman codes from txt file to array of pixels



############################## BATAS CODINGAN ASLI ##############################
        # # Convert image to pixels
        # matrix = imageToPixels(img)

        # # Convert matrix of pixels to image and save it
        # savedImage = pixelsToImage(matrix, filename)

        # # Getting runtime and compression percentage
        # endTime = timeit.default_timer()
        # endSize = os.stat(savedImage).st_size

        # print('\nRuntime program: ' + str(endTime - startTime) + " s")
        # print('Compression percentage: ' + str(endSize * 100 /startSize) + " %")        

# pixelsToImage([], "test")    