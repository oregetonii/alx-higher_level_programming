#!/usr/bin/python3
"""
Module 5-save_to_json_file

Contains function that writes an obj to file using JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Returns JSON representation of obj (string)
    Args:
        my_obj: python object to save to file
        filename: name of text file
    """
    import json

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
