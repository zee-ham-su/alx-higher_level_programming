#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    arr (list): The list of integers.

    Returns:
    int: A peak element in the list.

    Note:
    There may be more than one peak in the list.
    """
    def search_peak(low, high):
        if low == high:
            return list_of_integers[low]

        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            return search_peak(mid + 1, high)
        else:
            return search_peak(low, mid)

    if not list_of_integers:
        return None

    return search_peak(0, len(list_of_integers) - 1)
