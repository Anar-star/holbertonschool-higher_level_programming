#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    
    Args:
        data (dict): Python dictionary to serialize
        filename (str): Output JSON file name
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)  # Use indent for readability
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.
    
    Args:
        filename (str): Input JSON file name
    
    Returns:
        dict: Python dictionary with deserialized data
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading data from {filename}: {e}")
        return {}
