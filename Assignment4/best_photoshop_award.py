"""
File: best_photoshop_award.py
Name: Owen Zhangjian
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
THRESHOLD = 1.5


def main():
    """
    創作理念：個人蠻喜歡擁有諷刺題材的書籍或影視作品。在這張照片中，我用pycharm合成自己的愚蠢自拍和《侏羅紀世界：殞落國度》中的人造恐龍，
    試圖傳達出在當今世界中，部分人們常常不顧一切地被慾望和貪婪驅使，而將自己和他人暴露於危險當中而不自知，等到發生了劫難才後悔莫及。
    這張'Hello, Cutie; Bye, Dear World' 是用來告誡自己在做任何決定前，先理性思考並將慾望擱著。
    """
    self = SimpleImage('image_contest/Owen.JPG')  # 1170*869
    bg = SimpleImage('image_contest/Indoraptor.jpg')  # 1170*665
    bg.make_as_big_as(self)  # 1170*869
    new_img = combine(self, bg)
    new_img.show()


def combine(self, bg):
    for x in range(self.width):
        for y in range(self.height):
            self_pixel = self.get_pixel(x, y)
            bg_pixel = bg.get_pixel(x, y)
            avg = (self_pixel.red + self_pixel.blue + self_pixel.green) // 3
            total = self_pixel.red + self_pixel.blue + self_pixel.green
            if self_pixel.green > avg * THRESHOLD and total > 170:  # Green screen
                self_pixel.red = bg_pixel.red
                self_pixel.blue = bg_pixel.blue
                self_pixel.green = bg_pixel.green
    return self


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
