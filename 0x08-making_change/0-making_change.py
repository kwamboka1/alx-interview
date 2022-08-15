#!/usr/bin/python3
"""
A function to determine the fewest number of coins
"""


def makeChange(coins, total):
    """Given a pile of coins of different values"""
    temp = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0
    for coin in coins:
        if total % coin <= total:
            temp += total // coin
            total = total % coin

    return temp if total == 0 else -1
