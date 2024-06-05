#!/usr/bin/python3

""" A function that reads a text file"""


def read_file(filename=""):
    """A function that reads a text file"""
    with open (filename, "r", encoding="utf8") as f:
        content = f.read()
        for line in f:
            print(line, end='')

        
