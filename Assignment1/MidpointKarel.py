from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    put_outside_beepers()
    while front_is_clear():
        move_beeper_west()
        move_beeper_east()


"""
Will turn left two times.
"""
def double_turn():
    turn_left()
    turn_left()

"""

"""
def beeper_search():
    while no_beepers_present():
        if front_is_clear():
            move()
        if front_is_blocked():
            double_turn()
            if no_beepers_present():
                move()

"""

"""
def move_beeper_east():
    if facing_east():
        pick_beeper()
        move()
        if no_beepers_present():
            put_beeper()
        move()
        beeper_search()
        double_turn()

"""

"""
def move_beeper_west():
    if facing_west():
        move()
        if no_beepers_present():
            put_beeper()
        double_turn()
        move()
        pick_beeper()
        double_turn()
        move()
        move()
    beeper_search()
    double_turn()

"""

"""
def put_outside_beepers():
    move()
    put_beeper()
    while front_is_clear():
        move()
    double_turn()
    move()
    put_beeper()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
