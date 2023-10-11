""" Field status enumerator
"""

from enum import Enum


class FieldStatus():
    UNCHECKED = 0
    CLICKED = 1
    CONQUERED = 2
    EXPLODED = 3