#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class that inherits (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from a_class,
    but not if it is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
