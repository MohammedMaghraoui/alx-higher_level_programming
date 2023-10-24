#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Square:
     """Represent a square in a singly-linked list."""
         def __init__(self, size=0, position=(0, 0)):
              """Constructor.

        Args:
            size: length of a sde of the square.

        Raises:
            typeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the data of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the next_node of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(sele):
        """Get/set the next_node of the square."""
        return self.__size ** 2

    def my_print(self):
        """Get/set the next_node of the square."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Get/set the next_node of the square."""
        result = ""
        if self.__size == 0:
            return result
        for _ in range(self.__position[1]):
            result += "\n"
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result[:-1]  # Remove trailing newline

    def my_print(self):
        """Area of this square.

        Returns:
        The size square.
        """
        print(self)
