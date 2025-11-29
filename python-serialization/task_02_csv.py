#!/usr/bin/env python3
"""Convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and writes the contents into data.json in JSON format.
    Returns True if successful, otherwise False.
    """
    try:
        data_list = []

        # Read CSV file and convert each row to dictionary
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        # Save as JSON
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except Exception:
        return False
