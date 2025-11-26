#!/usr/bin/python3
"""
This module defines a function to check if an object is an instance of a class
or if it inherits from a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or of a class
    that inherited from a_class, else False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance or subclass instance of a_class,
              False otherwise.
    """
    return isinstance(obj, a_class)
