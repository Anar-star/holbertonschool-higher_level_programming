#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list in reverse order.

    Args:
        my_list: A list of integers. Defaults to an empty list.
    """
    # Check if the list is not None before attempting to reverse it
    if my_list is not None:
        # Create a reversed copy of the list.
        # This is a concise way to reverse the list.
        my_list.reverse()
        
        # Iterate through the reversed list
        for number in my_list:
            # Print the integer using the required str.format()
            print("{:d}".format(number))
