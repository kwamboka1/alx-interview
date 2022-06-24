#!/usr/bin/python3
""" Module containing function to unlock the lockboxes problem """


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be unlocked
    return: Bool -  True or False
    """
    keys = [0]
    for i in keys:
        for index in boxes[i]:
            if index not in keys and index < len(boxes):
                keys.append(index)
    if len(keys) == len(boxes):
        return True
    return False
