# universe_iterator creates every possible black and white image

import math
import random
import numpy as np
from PIL import Image

side = 100  # define the image's side in pixels
size = side ** 2  # calculate how many pixels are in the image


# transform a dec number to a bin number
# then strip two unnecessary zeros from the beginning of the bin number


def dec_to_bin(x):
    return bin(x)[2:]


# Take given variation of image in order (1, 2, 3, etc.), translate it
# into binary, and fill the rest with zeros up to the size of the image. 


def dipermutation(x, size):
    first_part_number = dec_to_bin(x)
    first_part = list(map(int, str(first_part_number)))
    to_be_filled = size - len(first_part)
    fill = list(map(int, np.zeros(to_be_filled)))
    return np.array(fill + first_part)


#  Assign colour black for 0 in the grid, and colour white for 1 in the grid


def number_to_color(numbers, x, y):
    if numbers[x, y] == 0:
        return (0, 0, 0)
    else:
        return (255, 255, 255)

order = random.randrange(2 ** (side * side) - 1)  # select random variation
diperm = dipermutation(order, size)  # create given variation of given size
shaped_numbers = diperm.reshape(side, side)  # create a side x side grid

img = Image.new('RGB', (side, side), "black")  # create new image
pixels = img.load()  # load its pixels


#  Assign colour for every pixel


for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = number_to_color(shaped_numbers, i, j)

img.show()  # show the image
