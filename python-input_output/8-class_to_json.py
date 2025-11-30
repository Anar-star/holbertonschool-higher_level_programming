#!/usr/bin/python3
"""Module that returns the dictionary description for JSON serialization
of a class instance.
"""


def class_to_json(obj):
    """Returns the dictionary representation of a class instance"""
    return obj.__dict__
