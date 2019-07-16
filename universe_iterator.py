# universe_iterator creates every possible black and white image

import random
import numpy as np
from PIL import Image

SIDE = 100  # define the image's side in pixels
SIZE = SIDE ** 2  # calculate how many pixels are in the image


# Transform a dec number to a bin number
# then strip two unnecessary zeros from the beginning of the bin number.
# Note: Returns a string.


def dec_to_bin(dec_number):
    return bin(dec_number)[2:]


# Take given variation of image (1, 2, 3, ...), translate it
# into binary, make a list of it, and fill the rest with zeros.
# Note: Our variation is put at the end of the number grid.


def get_number_grid(variation_number, size_of_grid):
    number = dec_to_bin(variation_number)
    digits_list = list(map(int, number))  # rewrite str to a list
    to_be_filled = size_of_grid - len(digits_list)
    number_grid = np.concatenate(
        [np.array(digits_list), np.zeros(to_be_filled, dtype=int)])
    return number_grid


#  Assign colour black for 0 in the grid, and colour white for 1 in the grid.


def number_to_color(shaped_grid, x_axis, y_axis):
    if shaped_grid[x_axis, y_axis] == 0:
        return (0, 0, 0)
    return (255, 255, 255)


ORDER = random.randrange(2 ** SIZE - 1)  # select random variation
NUMBER_GRID = get_number_grid(ORDER, SIZE)  # create given variation
SHAPED_GRID = NUMBER_GRID.reshape(SIDE, SIDE)  # create a SIDE x SIDE grid

IMG = Image.new('RGB', (SIDE, SIDE), "black")  # create new image
PIXELS = IMG.load()  # load its pixels


#  Assign colour for every pixel.


for x in range(IMG.size[0]):
    for y in range(IMG.size[1]):
        PIXELS[x, y] = number_to_color(SHAPED_GRID, x, y)

IMG.show()  # show the image
