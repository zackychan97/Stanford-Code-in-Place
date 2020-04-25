"""
Write a program to prompt the user for a weight on earth
and print the equivalent weight on the moon.
"""


def main():
    print("This program calculates a user's weight on the moon, given their weight on earth")
    earth_weight = float(input("Enter a weight on earth: "))
    MOON_WEIGHT = earth_weight * 0.165
    print("Equivalent weight on moon: " + str(MOON_WEIGHT))


if __name__ == '__main__':
    main()