"""
File: examplefor.py
------------------
Print the first 100 even numbers
"""

def main():
    for i in range(100):
        print(i * 2)

# Alternative solution that takes in a different range.
# 0 = start here, 200 = stop before here, 2 = skip by this much each time.
def alternative_solution():
    for i in range(0, 200, 2):
        print(i)
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()