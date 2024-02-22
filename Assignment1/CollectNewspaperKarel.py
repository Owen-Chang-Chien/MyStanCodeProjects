"""
File: CollectNewspaperKarel.py
Name: Owen Zhangjian
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel is at the start point located at Street 4, Avenue 3, facing East.
    Post-condition:Karel brings the newspaper to the start point, facing East.
    """
    move_to_the_newspaper()
    bring_the_newspaper_home()


def move_to_the_newspaper():
    """
    Karel goes out and picks the newspaper at Street 3, Avenue 6.
    """

    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()
    pick_beeper()


def bring_the_newspaper_home():
    """
    Karel brings the newspaper to the start point, facing East.
    """

    turn_around()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    """
    Karel turns left for 3 times.
    """

    for i in range(3):
        turn_left()


def turn_around():
    """
    Karel turns left for 2 times.
    """

    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
