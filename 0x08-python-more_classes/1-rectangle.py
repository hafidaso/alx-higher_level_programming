#!/usr/bin/python3

# 0-rectangle module
"""
This module contains a class Rectangle

>>> Rectangle = __import__('1-rectangle').Rectangle

>>> my_rectangle = Rectangle(2, 4)
>>> print(type(my_rectangle))
<class '1-rectangle.Rectangle'>

>>> dict_result = my_rectangle.__dict__
>>> print(dict(sorted(dict_result.items())))
{'_Rectangle__rect_height': 4, '_Rectangle__rect_width': 2}

"""

class Rectangle:
    """This is an class Rectangle with instance attributes height and width"""

    def __init__(self, width, height):
        """
        Initializes height and width of the rectangle
        upon creation of an instance using property
        getters and setters

        >>> my_rectangle = Rectangle(2, '4')
        Traceback (most recent call last):
            ...
        TypeError: height must be an integer

        >>> my_rectangle = Rectangle(0, 0)
        >>> my_rectangle.width = 10
        >>> my_rectangle.height = -3
        Traceback (most recent call last):
            ...
        ValueError: height must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for the width"""
        return self.__rect_width

    @width.setter
    def width(self, width):
        """
        Property setter for the width
        Checks if the type for the width is an integer or < 0
        If the above conditions aren't met errors are raised
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__rect_width = width

    @property
    def height(self):
        """Property getter for the height"""
        return self.__rect_height

    @height.setter
    def height(self, height):
        """
        Property setter for the height
        Checks if the type for the height is an integer or < 0
        If the above conditions aren't met errors are raised
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__rect_height = height


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

