#!/usr/bin/python3
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
    image_side (int): Holds the image side length in pixels.
    image_size (int): Holds the number of pixels in desired image.
    ordinal_number (int): The ordinal number of variation of an image.
    number_list (np.array): Containins digits 0 and 1 that represent pixels
        in the image.
    number_grid (np.array): Is the reshaped side x side array
        containing the numbers from the number_list.
    universe_iteration (Image):

Todo:
    * Finish writing the docs.
    * Save mechanism.
    * Update usage.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import sys
from typing import Tuple

from PIL import Image

import click

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


def create_digits_list(ordinal_number: int, image_size: int) -> np.array:
    """Create a digits list of an image variation.

    This function takes the ordinal number of given variation of image
    (e.g. 1, 2, 3), translates it into binary, makes a list of digits of it,
    and fills the rest of the list with zeros up to the size of the image.

    Args:
        ordinal_number: The ordinal number of variation of an image.
            E.g. image made of only 0 is the first variation;
            image made of 0 and 1 at the end is the second variation;
            image made of 0 and 10 at the end is the third variation.
        size_of_image: The number of pixels in the image.

    Returns:
        A one dimensional np.array containing digits 0 and 1 that represent
        pixels in the image. This array needs to be shaped in order to create
        the image.

    """
    number = dec_to_bin(ordinal_number)
    digits_list = list(map(int, number))  # rewrite str to a list[int]
    to_be_filled = image_size - len(digits_list)
    number_list = np.concatenate(
        [np.array(digits_list), np.zeros(to_be_filled, dtype=int)])
    return number_list


def number_to_colour(digit_in_grid: int) -> Tuple[int, int, int]:
    """Assign colour black for 0 in the grid, and colour white for 1 in the grid.

    Args:
        digit_in_grid: A digit in number grid that will represent a pixel.

    Returns:
        A tuple that holds the colour in RGB, either black (for 0)
        or white (for 1).

    """
    if digit_in_grid == 0:
        return (0, 0, 0)
    return (255, 255, 255)


def assign_colour(image: Image, number_grid: np.array) -> Image:
    """Assign colour for every pixel.

    Args:
        image:
        number_grid: Is the reshaped side x side array containing
        the numbers from the number_list.

    Returns:
        A coloured image.

    """
    pixels = image.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixels[x, y] = number_to_colour(
                number_grid[x, y])
    return image


@click.command()
@click.option(
    '-i',
    '--image_side',
    default=100,
    show_default=True,
    required=True,
    type=int,
    help='the side of an image')
@click.option(
    '-o',
    '--ordinal_number',
    required=True,
    multiple=True,
    type=int,
    help='select variation of an image')
def main(image_side: int, ordinal_number: int) -> None:
    """.

    Args:
        image_side:
        ordinal_number:

    Returns:
        Nothing.

    """
    if image_side > 1000:
        click.echo("The image's side cannot be larger than 1 000 px")
        sys.exit()

    image_size = image_side ** 2

    if ordinal_number > (2 ** image_size - 1):
        click.echo(
            'The ordinal number for side {} cannot be larger than {}'.format(
                image_side, (2 ** image_size - 1)))
        sys.exit()

    number_list = create_digits_list(ordinal_number, image_size)
    number_grid = number_list.reshape(image_side, image_side)

    universe_iteration = Image.new('RGB', (image_side, image_side), "black")
    universe_iteration = assign_colour(universe_iteration, number_grid)

    universe_iteration.show()


if __name__ == '__main__':
    main()
