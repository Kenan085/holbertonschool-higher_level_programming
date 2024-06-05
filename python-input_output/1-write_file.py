#!/usr/bin/python3

"""a function that writes a string to a text file """


def write_file(filename="", text=""):
    """A function that writes a string to a text file """
    with open(filename, 'w', 'utf8') as f:
        content = f.write(text)
        return content
