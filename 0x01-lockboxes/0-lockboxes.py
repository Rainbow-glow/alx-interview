#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    This function will take a list of lists and the content
    of a list will unlock other lists.
    
    Parameters:
    - boxes (list of lists): A list of lists where each inner list represents
    the keys contained in a box.

    The first box, boxes[0], is unlocked initially.

    Returns:
    - bool: True if all boxes can be opened using the keys contained in them,
    otherwise False.

    If the input list is empty, returns False.
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
