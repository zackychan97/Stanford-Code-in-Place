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
    1. First, Karel will put beepers and then move while her
    left is blocked, followed by a turn left and move forward.
    That same sequence just described will then repeat once more.

    2. Next, Karel will put beepers and then move while her
    left is blocked, after which she will turn left 3 times.

    3. Following this, Karel will repeat the first step.

    4. Next, Karel will repeat the second step.

    5. Following this, once again Karel will repeat Steps 1 and 3.

    6. Lastly, Karel will place a beeper and then move until she
    no longer has her left side blocked.
    """
    double_block_turn()
    block_tripleTurn()
    double_block_turn()
    block_tripleTurn()
    double_block_turn()
    blocked_left()

"""
Will place a beeper and move WHILE left is blocked, 
and then when it is not blocked will triple left turn.
"""
def block_tripleTurn():
        blocked_left()
        triple_turn()

"""
a FOR loop (2 times repeated): will place a beeper and move 
WHILE left is blocked, followed by a turn_move which is one 
left turn preceding one move, and then REPEAT the cycle again
"""
def double_block_turn():
        for i in range(2):
                blocked_left()
                turn_move()

"""
a FOR loop (3 times repeated): will place a beeper and move WHILE 
left is blocked, followed by a turn_move which is one left turn 
preceding one move, and then REPEAT the cycle again TWICE MORE
"""
def triple_block_turn():
        for i in range(3):
                blocked_left()
                turn_move()

"""
WHILE the left of Karel is blocked, Karel will first put a beeper,
and then Karel will move.
"""
def blocked_left():
    while left_is_blocked():
        put_beeper()
        move()

"""
first will turn Karel left, and then move Karel forward one corner
"""
def turn_move():
    turn_left()
    move()

"""
will turn Karel to the left 3 times
"""
def triple_turn():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
