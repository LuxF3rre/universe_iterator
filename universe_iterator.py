# -*- coding: utf-8 -*-

"""universe_iterator creates every possible black and white image.

Everything is represented among these images - your facebook photo, the Avatar
movie (as frames), the Bible, or even the picture of the very moment you read
this description.

Using default values, there is about 2^1000 possible images. Some of them
are just rotations of one another. Therefore, we can roughly estimate
that there are about (2^1000) / 4 unique images.

Example:
    $ python universe_iterator.py

Attributes:
    SIDE (int): Holds the image side length. There is only one constant
        holding the length of the side, therefore produced image can
        only be a square.
    SIZE (int): Holds the number of pixels in desired image.
    ORDER (int):
    NUMBER_LIST (np.array):
    NUMBER_GRID (np.array):
    IMG (Image):

Todo:
    * Finish writing the docs.
    * Add cli.
    * Save mechanism.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import random
from typing import Tuple

import click
from PIL import Image

import numpy as np


def dec_to_bin(dec_number: int) -> str:
    """Transform a dec number into a bin number.

    Args:
        dec_number: Decimal number to be translated into binary one.

    Returns:
        A binary number as a string. Before returning the value, transformed
        number is stripped form two zeros at the beggining.

    """
    return bin(dec_number)[2:]


def create_digits_list(variation_number: int, size_of_image: int) -> np.array:
    """Create a digits list of an image variation.

    This function takes the number of given variation of image (1, 2, 3, ...),
    translates it into binary, makes a list of digits of it, and fills
    the rest of the list with zeros up to the size of the image.

    Args:
        variation_number: The ordered number of variation of an image.
            E.g. images made of only 0 is the first variation;
            image made of 0 and 1 at the end is the second variation;
            image made of 0 and 10 at the end is the third variation.
        size_of_image: The number of pixels in the image.

    Returns:
        A one dimensional np.array containing digits 0 and 1 that represent
        pixels in image. This array needs to be shaped in order to create
        image.

    """
    number = dec_to_bin(variation_number)
    digits_list = list(map(int, number))  # rewrite str to a list(int)
    to_be_filled = size_of_image - len(digits_list)
    number_list = np.concatenate(
        [np.array(digits_list), np.zeros(to_be_filled, dtype=int)])
    return number_list


#  Assign colour black for 0 in the grid, and colour white for 1 in the grid.


def number_to_colour(digit_in_grid: int) -> Tuple[int, int, int]:
    """Assign colour to number.

    Args:
        digit_in_grid: A digit in number grid that will represent pixel.

    Returns:
        A tuple that holds the RGB colour, either black (for 0)
        or white (for 1).

    """
    if digit_in_grid == 0:
        return (0, 0, 0)
    return (255, 255, 255)


def assign_colour(image: Image, number_grid: np.array) -> Image:
    """Assign colour for every pixel.

    Args:

    Returns:

    """
    pixels = image.load()

    for x_pointer in range(image.size[0]):
        for y_pointer in range(image.size[1]):
            pixels[x_pointer, y_pointer] = number_to_colour(
                number_grid[x_pointer, y_pointer])
    return image


# Defaults


SIDE = 100
SIZE = SIDE ** 2
ORDER = random.randrange(2 ** SIZE - 1)  # select random variation

NUMBER_LIST = create_digits_list(ORDER, SIZE)
NUMBER_GRID = NUMBER_LIST.reshape(SIDE, SIDE)

IMG = Image.new('RGB', (SIDE, SIDE), "black")
IMG = assign_colour(IMG, NUMBER_GRID)

IMG.show()
