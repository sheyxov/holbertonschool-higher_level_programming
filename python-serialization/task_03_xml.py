#!/usr/bin/env python3
"""XML Serialization and Deserialization using ElementTree"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to a file.
    Returns True if successful, otherwise False.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.
    Returns the dictionary if successful, otherwise None.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary
    except Exception:
        return None

