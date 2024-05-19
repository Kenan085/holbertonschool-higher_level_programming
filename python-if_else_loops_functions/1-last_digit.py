#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def find_remainder(number):
    if number % 10 == 0:
        return 0
    if number > 0:
        return number % 10
    elif number < 10:
        return -(number % 10)

last_num = find_remainder(number)

if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")

