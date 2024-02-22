"""
File: blur.py
Name: Owen Zhangjian
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original image
    :return:new_img: the image being blurred
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    new_img.show()

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            # Todo: get pixel of new_img at x,y
    for x in range(new_img.width):
        for y in range(new_img.height):
            new_img_pixel = new_img.get_pixel(x, y)

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.

                red_0_0 = img.get_pixel(0, 0).red
                blue_0_0 = img.get_pixel(0, 0).blue
                green_0_0 = img.get_pixel(0, 0).green

                red_1_1 = img.get_pixel(1, 1).red
                blue_1_1 = img.get_pixel(1, 1).blue
                green_1_1 = img.get_pixel(1, 1).green

                red_0_1 = img.get_pixel(0, 1).red
                blue_0_1 = img.get_pixel(0, 1).blue
                green_0_1 = img.get_pixel(0, 1).green

                red_1_0 = img.get_pixel(1, 0).red
                blue_1_0 = img.get_pixel(1, 0).blue
                green_1_0 = img.get_pixel(1, 0).green

                new_r = (red_0_0 + red_1_1 + red_0_1 + red_1_0)/4
                new_b = (blue_0_0 + blue_1_1 + blue_0_1 + blue_1_0)/4
                new_g = (green_0_0 + green_1_1 + green_0_1 + green_1_0)/4
            elif x == img.width and y == 0:
                # Get pixel at the top-right corner of the image.

                red_w_0 = img.get_pixel(img.width, 0).red
                blue_w_0 = img.get_pixel(img.width, 0).blue
                green_w_0 = img.get_pixel(img.width, 0).green

                red_w1_0 = img.get_pixel(img.width-1, 0).red
                blue_w1_0 = img.get_pixel(img.width-1, 0).blue
                green_w1_0 = img.get_pixel(img.width-1, 0).green

                red_w_1 = img.get_pixel(img.width, 1).red
                blue_w_1 = img.get_pixel(img.width, 1).blue
                green_w_1 = img.get_pixel(img.width, 1).green

                red_w1_1 = img.get_pixel(img.width-1, 1).red
                blue_w1_1 = img.get_pixel(img.width-1, 1).blue
                green_w1_1 = img.get_pixel(img.width-1, 1).green

                new_r = (red_w_0 + red_w1_0 + red_w_1 + red_w1_1) / 4
                new_b = (blue_w_0 + blue_w1_0 + blue_w_1 + blue_w1_1) / 4
                new_g = (green_w_0 + green_w1_0 + green_w_1 + green_w1_1) / 4

            elif x == 0 and y == img.height:
                # Get pixel at the bottom-left corner of the image

                red_0_h = img.get_pixel(0, img.height).red
                blue_0_h = img.get_pixel(0, img.height).blue
                green_0_h = img.get_pixel(0, img.height).green

                red_0_h1 = img.get_pixel(0, img.height-1).red
                blue_0_h1 = img.get_pixel(0, img.height-1).blue
                green_0_h1 = img.get_pixel(0, img.height-1).green

                red_1_h = img.get_pixel(1, img.height).red
                blue_1_h = img.get_pixel(1, img.height).blue
                green_1_h = img.get_pixel(1, img.height).green

                red_1_h1 = img.get_pixel(1, img.height-1).red
                blue_1_h1 = img.get_pixel(1, img.height-1).blue
                green_1_h1 = img.get_pixel(1, img.height-1).green

                new_r = (red_0_h + red_0_h1 + red_1_h + red_1_h1) / 4
                new_b = (blue_0_h + blue_0_h1 + blue_1_h + blue_1_h1) / 4
                new_g = (green_0_h + green_0_h1 + green_1_h + green_1_h1) / 4

            elif x == img.width and y == img.height:
                # Get pixel at the bottom-right corner of the image

                red_w_h = img.get_pixel(img.width, img.height).red
                blue_w_h = img.get_pixel(img.width, img.height).blue
                green_w_h = img.get_pixel(img.width, img.height).green

                red_w1_h1 = img.get_pixel(img.width-1, img.height-1).red
                blue_w1_h1 = img.get_pixel(img.width-1, img.height-1).blue
                green_w1_h1 = img.get_pixel(img.width-1, img.height-1).green

                red_w1_h = img.get_pixel(img.width-1, img.height).red
                blue_w1_h = img.get_pixel(img.width-1, img.height).blue
                green_w1_h = img.get_pixel(img.width-1, img.height).green

                red_w_h1 = img.get_pixel(img.width, img.height-1).red
                blue_w_h1 = img.get_pixel(img.width, img.height-1).blue
                green_w_h1 = img.get_pixel(img.width, img.height-1).green

                new_r = (red_w_h + red_w1_h1 + red_w1_h + red_w_h1) / 4
                new_b = (blue_w_h + blue_w1_h1 + blue_w1_h + blue_w_h1) / 4
                new_g = (green_w_h + green_w1_h1 + green_w1_h + green_w_h1) / 4
 
            elif img.width > x > 0 and y == 0:
                # Get top edge's pixels (without two corners)

                red_x_0 = img.get_pixel(x, 0).red
                blue_x_0 = img.get_pixel(x, 0).blue
                green_x_0 = img.get_pixel(x, 0).green

                red_1x_0 = img.get_pixel(x + 1, 0).red
                blue_1x_0 = img.get_pixel(x + 1, 0).blue
                green_1x_0 = img.get_pixel(x + 1, 0).green

                red_1x_1 = img.get_pixel(x + 1, 1).red
                blue_1x_1 = img.get_pixel(x + 1, 1).blue
                green_1x_1 = img.get_pixel(x + 1, 1).green

                red_x_1 = img.get_pixel(x, 1).red
                blue_x_1 = img.get_pixel(x, 1).blue
                green_x_1 = img.get_pixel(x, 1).green

                red_x1_0 = img.get_pixel(x - 1, 0).red
                blue_x1_0 = img.get_pixel(x - 1, 0).blue
                green_x1_0 = img.get_pixel(x - 1, 0).green

                red_x1_1 = img.get_pixel(x - 1, 1).red
                blue_x1_1 = img.get_pixel(x - 1, 1).blue
                green_x1_1 = img.get_pixel(x - 1, 1).green

                new_r = (red_x_0 + red_1x_0 + red_1x_1 + red_x_1 + red_x1_0 + red_x1_1) / 6
                new_b = (blue_x_0 + blue_1x_0 + blue_1x_1 + blue_x_1 + blue_x1_0 + blue_x1_1) / 6
                new_g = (green_x_0 + green_1x_0 + green_1x_1 + green_x_1 + green_x1_0 + green_x1_1) / 6

            elif img.width > x > 0 and y == img.height:
                # Get bottom edge's pixels (without two corners)

                red_x_h = img.get_pixel(x, img.height).red
                blue_x_h = img.get_pixel(x, img.height).blue
                green_x_h = img.get_pixel(x, img.height).green

                red_1x_h = img.get_pixel(x + 1, img.height).red
                blue_1x_h = img.get_pixel(x + 1, img.height).blue
                green_1x_h = img.get_pixel(x + 1, img.height).green

                red_1x_h1 = img.get_pixel(x + 1, img.height-1).red
                blue_1x_h1 = img.get_pixel(x + 1, img.height-1).blue
                green_1x_h1 = img.get_pixel(x + 1, img.height-1).green

                red_x_h1 = img.get_pixel(x, img.height-1).red
                blue_x_h1 = img.get_pixel(x, img.height-1).blue
                green_x_h1 = img.get_pixel(x, img.height-1).green

                red_x1_h = img.get_pixel(x - 1, img.height).red
                blue_x1_h = img.get_pixel(x - 1, img.height).blue
                green_x1_h = img.get_pixel(x - 1, img.height).green

                red_x1_h1 = img.get_pixel(x - 1, img.height-1).red
                blue_x1_h1 = img.get_pixel(x - 1, img.height-1).blue
                green_x1_h1 = img.get_pixel(x - 1, img.height-1).green

                new_r = (red_x_h + red_1x_h + red_1x_h1 + red_x_h1 + red_x1_h + red_x1_h1) / 6
                new_b = (blue_x_h + blue_1x_h + blue_1x_h1 + blue_x_h1 + blue_x1_h + blue_x1_h1) / 6
                new_g = (green_x_h + green_1x_h + green_1x_h1 + green_x_h1 + green_x1_h + green_x1_h1) / 6

            elif x == 0 and img.height > y > 0:
                # Get left edge's pixels (without two corners)

                red_0_h = img.get_pixel(0, img.height).red
                blue_0_h = img.get_pixel(0, img.height).blue
                green_0_h = img.get_pixel(0, img.height).green

                red_0_h1 = img.get_pixel(0, img.height-1).red
                blue_0_h1 = img.get_pixel(0, img.height-1).blue
                green_0_h1 = img.get_pixel(0, img.height-1).green

                red_0_1h = img.get_pixel(0, img.height+1).red
                blue_0_1h = img.get_pixel(0, img.height+1).blue
                green_0_1h = img.get_pixel(0, img.height+1).green

                red_1_h1 = img.get_pixel(1, img.height - 1).red
                blue_1_h1 = img.get_pixel(1, img.height - 1).blue
                green_1_h1 = img.get_pixel(1, img.height - 1).green

                red_1_h = img.get_pixel(1, img.height).red
                blue_1_h = img.get_pixel(1, img.height).blue
                green_1_h = img.get_pixel(1, img.height).green

                red_1_1h = img.get_pixel(1, img.height + 1).red
                blue_1_1h = img.get_pixel(1, img.height + 1).blue
                green_1_1h = img.get_pixel(1, img.height + 1).green

                new_r = (red_0_h + red_0_h1 + red_0_1h + red_1_h1 + red_1_h + red_1_1h) / 6
                new_b = (blue_0_h + blue_0_h1 + blue_0_1h + blue_1_h1 + blue_1_h + blue_1_1h) / 6
                new_g = (green_0_h + green_0_h1 + green_0_1h + green_1_h1 + green_1_h + green_1_1h) / 6

            elif x == img.width and img.height > y > 0:
                # Get right edge's pixels (without two corners)

                red_w_h = img.get_pixel(img.width, img.height).red
                blue_w_h = img.get_pixel(img.width, img.height).blue
                green_w_h = img.get_pixel(img.width, img.height).green

                red_w_h1 = img.get_pixel(img.width, img.height - 1).red
                blue_w_h1 = img.get_pixel(img.width, img.height - 1).blue
                green_w_h1 = img.get_pixel(img.width, img.height - 1).green

                red_w_1h = img.get_pixel(img.width, img.height + 1).red
                blue_w_1h = img.get_pixel(img.width, img.height + 1).blue
                green_w_1h = img.get_pixel(img.width, img.height + 1).green

                red_w1_h1 = img.get_pixel(img.width-1, img.height - 1).red
                blue_w1_h1 = img.get_pixel(img.width-1, img.height - 1).blue
                green_w1_h1 = img.get_pixel(img.width-1, img.height - 1).green

                red_w1_h = img.get_pixel(img.width-1, img.height).red
                blue_w1_h = img.get_pixel(img.width-1, img.height).blue
                green_w1_h = img.get_pixel(img.width-1, img.height).green

                red_w1_1h = img.get_pixel(img.width-1, img.height + 1).red
                blue_w1_1h = img.get_pixel(img.width-1, img.height + 1).blue
                green_w1_1h = img.get_pixel(img.width-1, img.height + 1).green

                new_r = (red_w_h + red_w_h1 + red_w_1h + red_w1_h1 + red_w1_h + red_w1_1h) / 6
                new_b = (blue_w_h + blue_w_h1 + blue_w_1h + blue_w1_h1 + blue_w1_h + blue_w1_1h) / 6
                new_g = (green_w_h + green_w_h1 + green_w_1h + green_w1_h1 + green_w1_h + green_w1_1h) / 6

            else:
                # Inner pixels.

                red_x_y = img.get_pixel(x, y).red
                blue_x_y = img.get_pixel(x, y).blue
                green_x_y = img.get_pixel(x, y).green

                red_x_1y = img.get_pixel(x, y + 1).red
                blue_x_1y = img.get_pixel(x, y + 1).blue
                green_x_1y = img.get_pixel(x, y + 1).green

                red_x_y1 = img.get_pixel(x, y - 1).red
                blue_x_y1 = img.get_pixel(x, y - 1).blue
                green_x_y1 = img.get_pixel(x, y - 1).green

                red_x1_y = img.get_pixel(x-1, y).red
                blue_x1_y = img.get_pixel(x-1, y).blue
                green_x1_y = img.get_pixel(x-1, y).green

                red_x1_1y = img.get_pixel(x - 1, y + 1).red
                blue_x1_1y = img.get_pixel(x - 1, y + 1).blue
                green_x1_1y = img.get_pixel(x - 1, y + 1).green

                red_x1_y1 = img.get_pixel(x-1, y-1).red
                blue_x1_y1 = img.get_pixel(x-1, y-1).blue
                green_x1_y1 = img.get_pixel(x-1, y-1).green

                red_1x_y1 = img.get_pixel(x+1, y - 1).red
                blue_1x_y1 = img.get_pixel(x+1, y - 1).blue
                green_1x_y1 = img.get_pixel(x+1, y - 1).green

                red_1x_y = img.get_pixel(x+1, y).red
                blue_1x_y = img.get_pixel(x+1, y).blue
                green_1x_y = img.get_pixel(x+1, y).green

                red_1x_1y = img.get_pixel(x + 1, y + 1).red
                blue_1x_1y = img.get_pixel(x + 1, y + 1).blue
                green_1x_1y = img.get_pixel(x + 1, y + 1).green

                new_r = (red_x_y + red_x_1y + red_x_y1 + red_x1_y + red_x1_1y +
                         red_x1_y1 + red_1x_y1 + red_1x_y + red_1x_1y) / 9
                new_b = (blue_x_y + blue_x_1y + blue_x_y1 + blue_x1_y + blue_x1_1y +
                         blue_x1_y1 + blue_1x_y1 + blue_1x_y + blue_1x_1y) / 9
                new_g = (green_x_y + green_x_1y + green_x_y1 + green_x1_y + green_x1_1y +
                         green_x1_y1 + green_1x_y1 + green_1x_y + green_1x_1y) / 9
    return new_img


def main():
    """
    This function has one image processing algorithm: blur.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)  #blur*5
    blurred_img.show()


if __name__ == '__main__':
    main()
