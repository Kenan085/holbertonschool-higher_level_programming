#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer).

    Args:
        my_list: The list of integers.

    Returns:
        The sum of all unique integers in the list.
    """
    unique_nums = set(my_list)
    sum = 0
    for num in unique_nums:
        sum += num
    return sum
