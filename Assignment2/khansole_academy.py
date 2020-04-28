"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

PROBLEMS_REQUIRED = 3
MIN_RANDOM = 1
MAX_RANDOM = 99
RANDOM_NUMBER1 = random.randint(MIN_RANDOM, MAX_RANDOM)
RANDOM_NUMBER2 = random.randint(MIN_RANDOM, MAX_RANDOM)
ENTER_ANSWER = int(input("Enter the answer. "))

def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    teach_addition()

def teach_addition():
    print("What is " + str(RANDOM_NUMBER1) + " + " + str(RANDOM_NUMBER2) + "?")
    ENTER_ANSWER
    if ENTER_ANSWER == RANDOM_NUMBER1 + RANDOM_NUMBER2:

def ask_and_enter():
    for i in range(2):
        print("What is " + str(RANDOM_NUMBER1) + " + " + str(RANDOM_NUMBER2) + "?")
        ENTER_ANSWER




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
