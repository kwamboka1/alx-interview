#!usr/bin/python3

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
    i = 0

    while (now < n):
        pos = n - now

        if ( pos % now == 0):
            start = now
            now += start
            
            i += 2
        else:
            now += start
            i += 1

    return i
