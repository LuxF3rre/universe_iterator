# universe_iterator

This script generates every possible black and white image. Everything is represented among these images - your facebook photo, Avatar movie (as frames), the Bible, or even the picture of the very moment you read this description.

Using default values, there is about 2^1000 possible images. Some of them are just rotations of one another. Therefore, we can roughly estimate that there are about (2^1000) / 4 unique images.

## Requirements

- Python 3.7.1
- numpy 1.9.3
- Pillow 6.1.0

To install required modules run `pip3 install -r requirements.txt` in project directory.

## Usage

```Usage: universe_iterator.py [OPTIONS]

universe_iterator creates every possible black and white image.

Options:

  -i, --image_side INTEGER       the length of the side of the image in pixels >= 1  [default: 100]
                                 
  -o, --ordinal_numbers INTEGER  ordinal numbers of variation of the image >= 0  [required]
                                 
  --help                         Show this message and exit.

```

## Example result

![Example result]()
