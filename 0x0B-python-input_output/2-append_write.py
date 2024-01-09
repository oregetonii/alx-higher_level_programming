#!/usr/bin/python3
"""
Module 2-append_write

Contains function which appends text to end of file and returns num chars 
appended
"""


def append_write(filename="", text=""):
    """appends to text file and return num of chars appended"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
