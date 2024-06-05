#!/usr/bin/python3

"""a function that appends a string
at the end of a text file"""


def append_write(filename="", text=""):
    """Appending procedure"""
    with open(filename, 'a', encoding='utf8') as f:
        content = f.write(text)
        return content
