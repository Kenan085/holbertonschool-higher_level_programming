#!/usr/bin/python3

"""JSON Module"""
import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        return json.loads(f)
