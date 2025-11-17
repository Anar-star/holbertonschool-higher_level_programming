#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number and returns its value.
    The last digit is always positive (0-9).
    """
    
    # Calculate the last digit by taking the absolute value 
    # of the number modulo 10.
    last_digit = abs(number) % 10
    
    # Print the digit without a newline
    print(last_digit, end="")
    
    # Return the value of the last digit
    return last_digit
