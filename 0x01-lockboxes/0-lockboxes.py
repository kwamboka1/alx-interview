#!/usr/bin/python3
""" Module containing function to unlock the lockboxes problem """


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be unlocked
    return: Bool -  True or False
    """
    n = len(boxes)
    for box in boxes:
        if len(box) == 0 and box is not boxes[n-1]:
            return False
    for index, keys in enumerate(boxes):
        return True
