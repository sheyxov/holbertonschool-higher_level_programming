#!/usr/bin/python3
"""Script that adds arguments to a list and saves to add_item.json"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except Exception:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
