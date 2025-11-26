#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    Initialized with private size, validated.
    """

    def __init__(self, size):
        """
        Initialize a square with private size.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size <= 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self.__size
