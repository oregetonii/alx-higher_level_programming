#!/usr/bin/python3
"""
Module 7-add_item

Contains function that adds args to Python obj and saves to JSON file

# run with ./7-add_item.py
#
# cat add_item.json ; echo ""
# expect output: []
#
# ./7-add_item.py some random args
# cat add_item.json ; echo ""
# expect output: ["some", "random", "args"]

"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
        current_content = load_from_json_file(filename)
except FileNotFoundError:
        current_content = []

        save_to_json_file(current_content + argv[1:], filename)
