#!/usr/bin/python3

"""Module to use json"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

  Args:
    my_obj: The object to be serialized.

  Returns:
    str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
