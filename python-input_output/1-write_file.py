#!/usr/bin/python3
"""SAlam"""


def write_file(filename="", text=""):
    """Salam"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
