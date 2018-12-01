import math
import random
import numpy as np
from PIL import Image

side = 100 # image side in pixels
order = random.randrange(2**(side*side)-1) # choosing radomly which image to generate

size = side**2

def dec_to_bin(x):
    return int(bin(x)[2:])
    
def dipermutation(x, size):
    first_part_number = dec_to_bin(x)
    first_part = list(map(int, str(first_part_number)))
    to_be_filled = size - len(first_part)
    fill = list(map(int, np.zeros(to_be_filled)))
    return np.array(fill + first_part)
    
diperm = dipermutation(order, size)
    
def shape_numbers(x):
    return x.reshape((int(math.sqrt(size)), int(math.sqrt(size))))
    
shaped_numbers = shape_numbers(diperm) # creating side x side grid
    
def number_to_color(numbers, x, y):
    if numbers[x, y] == 0:
        return (0, 0, 0)
    else:
        return (255, 255, 255)

img = Image.new( 'RGB', (side, side), "black")
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = number_to_color(shaped_numbers, j, i)
img.show()


# test = Image.open("test.bmp")
# test_pixels = test.load()

#for i in range(test.size[0]):
#    for j in range(test.size[1]):
#        = pixels[i, j]