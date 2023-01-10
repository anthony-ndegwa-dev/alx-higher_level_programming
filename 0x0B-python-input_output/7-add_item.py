#!/usr/bin/python3
"""A script to add all arguments to a Python list, and save them to a file"""
import sys
import os.path


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

py_list = []
if os.path.exists('add_item.json'):
    py_list = load_file('add_item.json')

for arg in sys.argv[1:]:
    py_list.append(arg)

save_file(py_list, 'add_item.json')
