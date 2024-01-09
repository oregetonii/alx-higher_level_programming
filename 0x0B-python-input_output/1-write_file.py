#!/usr/bin/python3
"""
Module 1-write_file

Contains a function which writes string to file
"""


def write_file(filename="", text=""):
    """Write string to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return(f.write(text))
