#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
         """Constructor.

        Args:
            size: length of a sde of the square.

        Raises:
            typeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of this square.

        Returns:
        The size square.
        """
        return self.__size ** 2
