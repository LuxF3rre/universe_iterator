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

Todo:
    * Update usage.
    * Find a way to give filenames to all images.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import sys
from pathlib import Path
from typing import Tuple

from PIL import Image

import click

import numpy as np


def dec_to_bin(dec_number: int) -> str:
    """Transform a decimal number into a binary number.

    Args:
        dec_number: Decimal number to be translated into binary one.

    Returns:
        A binary number as a string.

    """
    return bin(dec_number)[2:]


def create_digits_list(ordinal_number: int, image_size: int) -> np.array:
    """Create a digits list of an image variation from ordinal number.

    Args:
        ordinal_number: The ordinal number of variation of an image.
            E.g. image made of only 0 is the first variation;
            image made of 0 and 1 at the end is the second variation;
            image made of 0 and 10 at the end is the third variation.
        size_of_image: The number of pixels in the image.

    Returns:
        A one dimensional np.array that represent pixels in the image.

    """
    number = dec_to_bin(ordinal_number)
    digits_list = list(map(int, number))  # rewrite str to a list[int]
    to_be_filled = image_size - len(digits_list)
    number_list = np.concatenate(
        [np.array(digits_list), np.zeros(to_be_filled, dtype=int)])
    return number_list


def number_to_colour(digit_in_grid: int) -> Tuple[int, int, int]:
    """Return colour for given number.

    Args:
        digit_in_grid: A digit in number grid that will represent a pixel.

    Returns:
        A tuple that holds the colour in RGB.

    """
    if digit_in_grid == 0:
        return (0, 0, 0)
    return (255, 255, 255)


def assign_colour(image: Image, number_grid: np.array) -> Image:
    """Assign colour for every pixel.

    Args:
        image: Image to be coloured.
        number_grid: Holds the reshaped array of digits.

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
    type=int,
    help='the length of the side of the image')
@click.option(
    '-o',
    '--ordinal_numbers',
    required=True,
    multiple=True,
    type=int,
    help='ordinal numbers of variation of the image')
def main(image_side: int, ordinal_numbers: Tuple[int]) -> None:
    """universe_iterator creates every possible black and white image.

    Everything is represented among these images - your facebook photo,
    the Avatar movie (as frames), the Bible, or even the picture
    of the very moment you read his description.

    Using default values, there is about 2^1000 possible images. Some of them
    are just rotations of one another. Therefore, we can roughly estimate
    that there are about (2^1000) / 4 unique images.

    """
    # Check if passed options are correct or sane.

    if image_side > 1000:
        click.echo("Error: The image's side cannot be larger than 1 000 px.")
        sys.exit()

    image_size = image_side ** 2

    for ordinal_number in ordinal_numbers:
        if ordinal_number > (2 ** image_size - 1):
            click.echo(
                'Error: The ordinal number for side {}'
                'cannot be larger than {}'.format(
                    image_side, '{:.2e}'.format((2 ** image_size - 1))))
            sys.exit()

        # Create the image and save it.

        number_list = create_digits_list(ordinal_number, image_size)
        number_grid = number_list.reshape(image_side, image_side)

        universe_iteration = Image.new(
            'RGB', (image_side, image_side), "black")
        universe_iteration = assign_colour(universe_iteration, number_grid)

        save_path = Path(__file__).resolve().parent
        save_path = save_path / 'Img.png'

        universe_iteration.save(save_path, 'PNG')
        print('Created universe iteration as ./Img.png')


if __name__ == '__main__':
    main()
