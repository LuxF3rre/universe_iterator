# -*- coding: utf-8 -*-

"""universe_iterator creates every possible black and white image.

Everything is represented among these images - your facebook photo, the Avatar movie (as frames), the Bible, or even the picture of the very moment you read this description.

Using default values, there is about 2^1000 possible images. Some of them are just rotations of one another. Therefore, we can roughly estimate that there are about (2^1000) / 4 unique images.

Example:
    $ python universe_iterator.py

Attributes:
    SIDE (int): Holds the image side lenght. There is only one constant holding the lenght of the side, therefore produced image can only be a square.
    SIZE (int): Holds the numer of pixels in desired image.
    ORDER ():
    NUMBER_LIST ():
    UMBER_GRID ():
    IMG ():
    PIXELS ():

Todo:
    * Finish writing the docs.
    * Remove the "line too long" warnings from pylint and pycodestyle.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import random
import numpy as np
from PIL import Image

SIDE = 100
SIZE = SIDE ** 2


def dec_to_bin(dec_number: int) -> str:
    """Transforms a dec number into a bin number.

    Args:
        dec_number: Decimal number to be translated into binary one.

    Returns:
        A binary number as a string. Before returning the value, transformed number is stripped form two zeros at the beggining.

    """
    return bin(dec_number)[2:]


def create_digits_list(variation_number: int, size_of_image: int) -> np.array:
    """Creates a digits list of given image variation.

    This function takes the number of given variation of image (1, 2, 3, ...), translates it into binary, makes a list of digits of it, and fills the rest of the list with zeros up to the size of the image.

    Args:
        variation_number: The ordered number of variation of an image.
            E.g. images made of only 0 is the first variation; image made of 0 and 1 at the end is the second variation; image made of 0 and 10 at the end is the third variation.
        size_of_image: The number of pixels in the image.

    Returns:


    """
    number = dec_to_bin(variation_number)
    digits_list = list(map(int, number))  # rewrite str to a list
    to_be_filled = size_of_image - len(digits_list)
    number_list = np.concatenate(
        [np.array(digits_list), np.zeros(to_be_filled, dtype=int)])
    return number_list


#  Assign colour black for 0 in the grid, and colour white for 1 in the grid.


def number_to_color(number_grid: np.array, x_axis: int, y_axis: int) -> tuple(int):
    """

    Args:
        number_grid:
        x_axis:
        y_axis:

    Returns:

    """
    if number_grid[x_axis, y_axis] == 0:
        return (0, 0, 0)
    return (255, 255, 255)


ORDER = random.randrange(2 ** SIZE - 1)  # select random variation
NUMBER_LIST = create_digits_list(ORDER, SIZE)  # create given variation
NUMBER_GRID = NUMBER_LIST.reshape(SIDE, SIDE)  # create a SIDE x SIDE grid

IMG = Image.new('RGB', (SIDE, SIDE), "black")  # create new image
PIXELS = IMG.load()  # load its pixels


#  Assign colour for every pixel.


for x in range(IMG.size[0]):
    for y in range(IMG.size[1]):
        PIXELS[x, y] = number_to_color(NUMBER_GRID, x, y)

IMG.show()  # show the image
