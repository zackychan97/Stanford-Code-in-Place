from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move()
    triple_turn_left()
    move()
    turn_left()
    double_jump()
    pick_beeper()
    double_left_turn()
    triple_jump()
    triple_turn_left()
    move()
    triple_turn_left()



# Original World get Newspaper Function
# def get_the_news():
#     while front_is_clear():
#         move()
#         triple_turn_left()
#         move()
#         turn_left()
#         double_jump()
#         pick_beeper()
#         double_left_turn()
#         triple_jump()
#         triple_turn_left()
#         move()
#         triple_turn_left()

# Turns
def triple_turn_left():
    turn_left()
    turn_left()
    turn_left()

def double_left_turn():
    turn_left()
    turn_left()

# Jumps
def double_jump():
    move()
    move()

def triple_jump():
    move()
    move()
    move()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
