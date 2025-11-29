#!/usr/bin/python3
"""Salam"""


def append_write(filename="", text=""):
    """Salam"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
