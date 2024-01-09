#!/usr/bin/python3
"""
Module 0-read_file

Contains a function that reads and prints contents of file.
"""


def read_file(filename=""):
    """Read and print text in a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
