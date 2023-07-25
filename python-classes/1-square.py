#!/usr/bin/python3
"""Definition for a square"""


class Square:
    """A square with a private
    instance size
    """
    __size = 0

    def __init__(self, value):
        """
        Arguments:
             value (num): int value
        """
        self.__size = value
