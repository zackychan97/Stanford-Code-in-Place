from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    turn_left()
    beeper_or_move()
    double_turn()
    beeper_or_move()
    blocked()

    quad_jump()
    turn_left()
    beeper_or_move()
    double_turn()
    beeper_or_move()
    blocked()

    quad_jump()
    turn_left()
    beeper_or_move()
    double_turn()
    beeper_or_move()
    blocked()

    quad_jump()
    turn_left()
    beeper_or_move()
    double_turn()
    beeper_or_move()
    blocked()

def place_beeper_move():
    while no_beepers_present():
        put_beeper()
        move()

def move_until_blocked():
    while front_is_clear():
        move()

def beeper_or_move():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()

def blocked():
    while front_is_blocked():
        if no_beepers_present():
            put_beeper()
        else:
            turn_left()

def triple_turn():
    for i in range(3):
        turn_left()

def double_turn():
    for i in range(2):
        turn_left()

def quad_jump():
    for i in range(4):
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
