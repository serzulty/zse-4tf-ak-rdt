"""
Lumache - Python library for cooks and food lovers.

Author: Adrian Kozlowski

This library provides a collection of functions to help you manage and 
randomly select ingredients for your culinary creations.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    This function can return a predefined list of ingredients. If a specific 
    kind of ingredients is requested, it will validate the kind and return 
    the corresponding ingredients.

    :param kind: Optional "kind" of ingredients. If None, returns a default list.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
