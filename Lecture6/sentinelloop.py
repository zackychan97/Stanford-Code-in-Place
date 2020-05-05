"""
File: sentinelloop.py
------------------
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
import random

def main():
    total = 0
    print("We are going to roll two dice.")
    roll = str(input("Type: 'Roll' to roll the dice, type anything else to quit. "))
    while roll == "Roll":
        dice1 = random.randint(1, 6)
        print("Dice 1: ", dice1)
        dice2 = random.randint(1, 6)
        print("Dice 2: ", dice2)
        total = total + dice1 + dice2
        print("Total: ", total)
        roll = str(input("Type: 'Roll' to roll the dice, type anything else to quit. "))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()