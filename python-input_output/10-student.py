#!/usr/bin/python3

"""Student Class"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """JSON Class"""
        if attrs is None:
            return {key: value for key, value in self.__dict__.items()}
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
