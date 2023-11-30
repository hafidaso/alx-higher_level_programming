#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = low + (high - low) // 2

        # Check if mid is greater than its neighbors
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]

        # If the middle element is less than its left neighbor, then peak lies in left half
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid
        else:
            # If the middle element is less than its right neighbor, then peak lies in right half
            low = mid + 1

    return list_of_integers[low]
