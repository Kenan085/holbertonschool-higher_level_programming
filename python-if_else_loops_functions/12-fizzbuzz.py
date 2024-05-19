#!/usr/bin/python3
def fizzbuzz():
    for k in range(1, 101):
        if k % 15 == 0:
            print("FizzBuzz", end=" ")
            continue
        elif k % 5 == 0:
            print("Buzz", end=" ")
            continue
        elif k % 3 == 0:
            print("Fizz", end=" ")
            continue
        else:
            print(k, end=" ")
            continue
