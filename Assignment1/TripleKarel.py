from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    blocked_left()
    turn_move()
    blocked_left()
    turn_move()
    blocked_left()
    triple_turn()
    blocked_left()
    turn_move()
    blocked_left()
    turn_move()
    blocked_left()
    triple_turn()
    blocked_left()
    turn_move()
    blocked_left()
    turn_move()
    blocked_left()

    # double_block_turn()
    # block_tripleTurn()
    # double_block_turn()
    # triple_turn()
    # double_block_turn()
    # blocked_left()


def block_tripleTurn():
        blocked_left()
        triple_turn()

def doubleBlock_tripleTurn():
        for i in range(2):
                blocked_left()
                triple_turn()


def double_block_turn():
        for i in range(2):
                blocked_left()
                turn_move()


def triple_block_turn():
        for i in range(3):
                blocked_left()
                turn_move()


def blocked_left():
    while left_is_blocked():
        put_beeper()
        move()


def blocked_right():
    while right_is_blocked():
        put_beeper()
        move()


def turn_move():
    turn_left()
    move()


def triple_turn():
    turn_left()
    turn_left()
    turn_left()


def move_while_clear():
    while front_is_clear():
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
