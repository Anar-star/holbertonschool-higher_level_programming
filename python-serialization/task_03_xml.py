#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary: dict, filename: str):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The XML filename to write.
    """
    root = ET.Element("data")  # root element

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # store value as string

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception as e:
        print(f"Error writing XML file: {e}")


def deserialize_from_xml(filename: str) -> dict:
    """
    Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text  # store as string
        return result

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except ET.ParseError:
        print(f"Error: Failed to parse '{filename}'.")
        return {}
