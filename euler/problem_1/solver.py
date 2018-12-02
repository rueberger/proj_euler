"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def solve():
    """ A streaming solution with constant memory usage is possible, this is cleaner
    """
    multiples_of_3 = set(range(0, 1000, 3))
    multiples_of_5 = set(range(0, 1000, 5))
    multiples_of_either = multiples_of_3.union(multiples_of_5)
    return sum(multiples_of_either)
