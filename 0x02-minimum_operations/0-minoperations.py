#!/usr/bin/python3

"""
    A method that determines the number of minmum operations given n characters

"""

def minOperations(n):
    """
        A function that calculates the fewest number of operations needed to giv        e a result of exactly n H characters in a file
        args: n: Number of characters to be displayed

        return:
                number of min operations
    """

    now = 1
    start = 0
    count = 0
    while now < n:
        rem = n - now
        if ( rem % now == 0):
            start = now
            now += start
            count += 2
        else:
            now += start
            count += 1
    return count


