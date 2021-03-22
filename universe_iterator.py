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
    $ python universe_iterator.py 2137 314 512

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import sys
from pathlib import Path
from typing import Tuple

import click

from PIL import Image

import numpy as np


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
    number = bin(ordinal_number)
    # rewrite number to a list of ints
    digits_list = list([int(x) for x in number[2:]])
    to_be_filled = image_size - len(digits_list)
    number_list = np.concatenate(
        [np.zeros(to_be_filled, dtype=int)], np.array(digits_list))
    return number_list


def number_to_colour(digit_in_grid: int) -> Tuple[int, int, int]:
    """Return colour for a given number.

    Args:
        digit_in_grid: A digit in number grid that will represent a pixel.

    Returns:
        A tuple that holds the colour in RGB.

    """
    if digit_in_grid:
        return (255, 255, 255)
    return (0, 0, 0)


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
    help='the length of the side of the image in pixels')
@click.argument(
    'ordinal_numbers',
    nargs=-1,
    type=int)
def main(image_side: int, ordinal_numbers: Tuple[int]) -> None:
    """universe_iterator creates every possible black and white image.

    Everything is represented among these images - your facebook photo,
    the Avatar movie (as frames), the Bible, or even the picture
    of the very moment you read his description.

    For ORDINAL_NUMBERS specify ordinal numbers of variations
    of the images you want to create.

    """
    # Check if passed options are correct or sane.

    if not 0 < image_side <= 1000:
        click.echo("Error: The image's side must be between 1 and 1 000 px.")
        sys.exit()

    image_size = image_side ** 2

    for index, ordinal_number in enumerate(ordinal_numbers):
        if not 0 <= ordinal_number <= max_number := (2 ** image_size - 1):
            click.echo(
                'Error: The ordinal number for side {} '
                'must be at least 0 and cannot be larger than {}'.format(
                    image_side, '{:.2e}'.format(max_number)))
            sys.exit()

        # Create the image and save it.

        number_list = create_digits_list(ordinal_number, image_size)
        number_grid = number_list.reshape(image_side, image_side)

        universe_iteration = Image.new(
            'RGB', (image_side, image_side), 'black')
        universe_iteration = assign_colour(universe_iteration, number_grid)

        save_path = Path(__file__).resolve().parent
        save_path = save_path / 'output{}.png'.format(index)

        universe_iteration.save(save_path, 'BMP')
        print('Created universe iteration as ./output{}.bmp'.format(index))


if __name__ == '__main__':
    main()
