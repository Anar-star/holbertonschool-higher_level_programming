#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list safely.

    Args:
        my_list: The list to retrieve the element from.
        idx: The index of the element to retrieve.

    Returns:
        The element at the given index, or None if the index is invalid.
    """
    # 1. Check for negative index
    if idx < 0:
        return None

    # 2. Check for index out of range (index must be less than the list length)
    if idx >= len(my_list):
        return None

    # 3. If the index is valid, retrieve and return the element
    return my_list[idx]
