#!/usr/bin/python3
"""
Module 4- from_json_string

Contains function that returns obj represented by JSON string
"""


def from_json_string(my_str):
    """Returns obj reppresented by JSON string
    Args:
        my_str: JSON string
    Return:
        obj (python data structure)
    """
    import json

    return json.load(my_str)
