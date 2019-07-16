# universe_iterator creates every possible black and white image

import random
import numpy as np
from PIL import Image

SIDE = 100  # define the image's side in pixels
SIZE = SIDE ** 2  # calculate how many pixels are in the image


# Transform a dec number to a bin number
# then strip two unnecessary zeros from the beginning of the bin number.
# Note: Returns a string.


def dec_to_bin(x):
    return bin(x)[2:]


# Take given variation of image (1, 2, 3, ...), translate it
# into binary, make a list of it, and fill the rest with zeros.
# Note: Our variation is put at the end of the number grid.


def get_variations(x, size):
    variation = dec_to_bin(x)
    variation_list = list(map(int, variation))  # rewrite str to a list
    to_be_filled = size - len(variation_list)
    number_grid = np.concatenate([np.array(variation_list), np.zeros(to_be_filled, dtype=int)])
    return number_grid


#  Assign colour black for 0 in the grid, and colour white for 1 in the grid.


def number_to_color(numbers, x, y):
    if numbers[x, y] == 0:
        return (0, 0, 0)
    return (255, 255, 255)


order = random.randrange(2 ** SIZE - 1)  # select random variation
variation = get_variations(order, SIZE)  # create given variation
shaped_variation = variation.reshape(SIDE, SIDE)  # create a SIDE x SIDE grid

img = Image.new('RGB', (SIDE, SIDE), "black")  # create new image
pixels = img.load()  # load its pixels


#  Assign colour for every pixel.


for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = number_to_color(shaped_variation, i, j)

img.show()  # show the image
