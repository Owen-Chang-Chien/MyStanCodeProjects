"""
File: mirror_lake.py
Name: Owen Zhangjian
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:str, 'images/mt-rainier.jpg'
    :return: SimpleImage, the image that have a mirror vibe together with the original one
    """
    ref = SimpleImage(filename)
    b_img = SimpleImage.blank(ref.width, ref.height*2)
    b_img.show()
    for x in range(ref.width):
        for y in range(ref.height):

            colored_pixel = ref.get_pixel(x, y)
            upper_blank_pixel = b_img.get_pixel(x, y)
            lower_blank_pixel = b_img.get_pixel(x, (b_img.height-1)-y)

            upper_blank_pixel.red = colored_pixel.red
            upper_blank_pixel.blue = colored_pixel.blue
            upper_blank_pixel.green = colored_pixel.green

            lower_blank_pixel.red = colored_pixel.red
            lower_blank_pixel.blue = colored_pixel.blue
            lower_blank_pixel.green = colored_pixel.green

    return b_img


def main():
    """
    This function has one image processing algorithm: reflect.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
