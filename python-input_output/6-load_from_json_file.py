#!/usr/bin/python3
"""Module that creates a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Loads a Python object from a file containing JSON data"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
