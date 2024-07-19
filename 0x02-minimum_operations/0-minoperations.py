#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    """

    simp = 1
    start = 0
    count = 0
    while simp < n:
        remainder = n - simp
        if (remainder % simp == 0):
            start = simp
            simp += start
            count += 2
        else:
            simp += start
            count += 1
    return count
