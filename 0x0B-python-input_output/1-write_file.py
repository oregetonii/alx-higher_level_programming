#!/usr/bin/python3
"""
Module 1-write_file

Contains a function which writes to text file and returns num chars written
"""


def write_file(filename="", text=""):
    """writes to text file and return num of chars written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return(f.write(text))
