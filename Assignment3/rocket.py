"""
File: rocket.py
Name:Owen Zhangjian
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():

    """
    This program is designed to draw ASCII art - a rocket. Users could change the constant
    defined as SIZE at top of the file to determine the size of the rocket.
    """

    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    This function could generate the head of a rocket. The head part of this rocket art is composed of the signs '/' and
     '\'.
    """

    for i in range(SIZE):

        for j in range(-i+SIZE):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print("\\", end='')

        print('')


def belt():

    """
    This function could generate a belt, which connects the head and the upper part of a rocket. It could also connect
    the lower part and the head of a rocket. This belt is composed of the signs '+' and '='.
    """

    for i in range(1):
        print('+', end='')
    for i in range(2 * SIZE):
        print('=', end='')
    for i in range(1):
        print('+', end='')

    print('')


def upper():

    """
    This function generates the upper part of a rocket. The upper part of this ASCII art is composed of these signs '|',
    '.', and '/\'.
    """

    for i in range(SIZE):

        for j in range(1):
            print('|', end='')
        for j in range(-i+(SIZE-1)):
            print('.', end='')
        for j in range(i+1):
            print('/\\', end='')
        for j in range(-i+(SIZE-1)):
            print('.', end='')
        for j in range(1):
            print('|', end='')

        print('')


def lower():
    """
    This function generates the lower part of a rocket. The lower part of this ASCII art is composed of these signs '|',
    '.', '\', and '/'.
    """

    for i in range(SIZE):

        for j in range(1):
            print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(-i+SIZE):
            print('\\/', end='')
        for j in range(i):
            print('.', end='')
        for j in range(1):
            print('|', end='')

        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
