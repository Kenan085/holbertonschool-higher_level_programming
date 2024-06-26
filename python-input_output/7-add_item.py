#!/usr/bin/python3

"""Module for creating script"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    for i in range(1, len(sys.argv)):
        existing_data.append(sys.argv[i])

    save_to_json_file(existing_data, "add_item.json")

    return load_from_json_file("add_item.json")


if __name__ == "__main__":
    main()
