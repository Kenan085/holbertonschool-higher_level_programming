#!/usr/bin/python3

def print_last_digit(number):
    if number > 0:
        remainder = number % 10
    elif number == 0:
        remainder = 0
    else:
        remainder = -(number % 10 - 10)

    print(f"{remainder}", end='')

    return remainder
