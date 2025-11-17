#!/usr/bin/python3
# This program prints numbers 00 to 99, separated by a comma and a space,
# using only one loop and a single print function to respect the 'max 2 prints' constraint.

# A string buffer is necessary to satisfy the 'max 2 print' rule,
# allowing the full output to be printed in one call.
s = ""

# Loop from 0 up to 99.
for i in range(100):
    # Use string formatting to ensure the number is always two digits (e.g., 5 -> "05").
    formatted_num = "{:02d}".format(i)

    # Append the number to the string buffer.
    s += formatted_num

    # Append the required separator (", ") only if it is NOT the last number (99).
    if i < 99:
        s += ", "

# Use the single print function with string format to output the entire accumulated string.
print("{}".format(s))
