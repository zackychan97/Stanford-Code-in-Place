"""
Write a program to simulate a magic eight ball. The program should
repeatedly prompt the user to type in a yes or no question and
give a random answer from a set predetermined answers.
"""

import random

MIN_INT = 1
MAX_INT = 5


def main():
    question = str(input("Ask Python a question, any question you desire the answer to. "))
    while question != "":
        answer_question()
        question = str(input("Ask Python a question, any question you desire the answer to. "))


def answer_question():
    question_number = random.randint(MIN_INT, MAX_INT)
    if question_number == 1:
        print("As I see it, yes.")
    elif question_number == 2:
        print("Ask again later.")
    elif question_number == 3:
        print("Better not tell you now.")
    elif question_number == 4:
        print("Cannot predict now.")
    else:
        print("Concentrate and ask again.")


if __name__ == '__main__':
    main()