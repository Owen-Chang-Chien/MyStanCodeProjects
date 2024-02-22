"""
File: CheckerboardKarel.py
Name: Owen Zhangjian
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition:Karel stays at (1,1) without doing anything.
    Post-condition: Karel finishes drawing a checkerboard by placing beepers.

    I had some discussion with my TA HuaJung Chang on this task. She told me to fix some problems because my code didn't
    work with 40*40 blocks. However, I still got no clues. I am here to say sorry to my TA. I cannot figure it out
    before deadline.
    """

    put_beeper()
    fill_one_line()
    fill_one_line_2()

    if on_beeper():
        turn_right()
        pick_beeper()

    fix_the_mistakes()

    if facing_north():
        if front_is_clear():
            move()
            turn_right()
            put_beeper()
            fill_one_line()

    fill_one_line_2()

    if not front_is_clear():
        pass
    if not left_is_clear():
        if on_beeper():
            turn_right()
            pick_beeper()

    fix_the_mistakes()

    if facing_north():
        if front_is_clear():
            move()
            turn_right()
            put_beeper()
            fill_one_line()

    fill_one_line_2()

    if not front_is_clear():
        pass
    if not left_is_clear():
        if on_beeper():
            turn_right()
            pick_beeper()

    fix_the_mistakes()

    if facing_north():
        if front_is_clear():
            move()
            turn_right()
            put_beeper()
            fill_one_line()

    fill_one_line_2()


def turn_right():
    # Karel will turn right for three times.

    turn_left()
    turn_left()
    turn_left()


def turn_around():
    # Karel will turn left for two times.

    turn_left()
    turn_left()


def fill_one_line():
    # Karel will face east put one beeper every two blocks.

    while facing_east():
        if not front_is_clear():
            pass
        if front_is_clear():
            move()
        if front_is_clear():
            move()
            put_beeper()
        if not front_is_clear():
            turn_left()


def fill_one_line_2():
    # This time, when Karel faces west, it will put one beeper every two blocks.

    while facing_north():
        if front_is_clear():
            move()
            turn_left()
            put_beeper()

    while facing_west():
        if not front_is_clear():
            pass
        if front_is_clear():
            move()
        if front_is_clear():
            move()
            put_beeper()
        if not front_is_clear():
            turn_right()


def fix_the_mistakes():
    # If Karel puts a beeper on wrong spots on one avenue, it will walk this avenue again and fix its mistakes.

    while facing_east():
        if front_is_clear():
            move()
            put_beeper()
        if front_is_clear():
            move()
            pick_beeper()
        if not front_is_clear():
            turn_around()
            while front_is_clear():
                move()
            turn_right()


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    execute_karel_task(main)
