#!/usr/bin/python3
# This function prints all integers of a list, one per line.
# It uses a for loop to iterate through the list and str.format() for printing.
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list.

    Args:
        my_list: A list of integers. Defaults to an empty list.
    """
    # Iterate through each element in the provided list.
    for number in my_list:
        # Use str.format() to print the integer.
        # The placeholder '{}' is replaced by the value of 'number'.
        # This fulfills the requirement of using str.format().
        print("{:d}".format(number))
