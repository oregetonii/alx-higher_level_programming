#!/usr/bin/python3
"""
Module 6-load_from_json_file

Contains function that creates an obj from JSON file
"""


def load_from_json_file(filename):
    """Returns JSON representation of obj (string)
    Args:
        filename: name of text file
    """
    import json

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
