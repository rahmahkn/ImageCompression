import math
from PIL import Image

# Function to convert percentage to number of vectors
def percentToNb(percent, w, h):
    return int(math.ceil((percent * w * h * 0.01) / (w + h + 1)))

# Function to save image with certain name
def saveImage(arr, name):
    return Image.fromarray(arr).save(name)

# Function to 


# print(percentToNb(3.2, 3900, 2600))