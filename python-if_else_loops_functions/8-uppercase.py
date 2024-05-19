#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in range(len(str)):
        if 97 <= ord(str[i]) and 122 >= ord(str[i]):
            new_str += chr(ord(str[i]) - 32)
        else:
            new_str += str[i]
    print("{}\n".format(new_str), end='')

