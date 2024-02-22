"""
File: fire.py
Name: Owen Zhangjian
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param : filename:str, 'images/greenland-fire.png'
    :return: SimpleImage, the image that highlight the fire for better observation.
    """
    new_fire = SimpleImage(filename)

    for pixel in new_fire:
        avg = (pixel.red + pixel.blue + pixel.green) // 3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg

    return new_fire


def main():
    """
    This function has one image processing algorithm: highlight_fires
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
