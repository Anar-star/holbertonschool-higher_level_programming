#!/usr/bin/python3
# This program prints the lowercase ASCII alphabet, without a final newline.

output_string = ""

# Loop from the ASCII value of 'a' (97) up to and including 'z' (122).
# We use the integer values directly since storing characters is disallowed.
for i in range(97, 123):
    # chr(i) converts the ASCII integer back into its character equivalent.
    output_string += chr(i)

# Print the final string containing the entire alphabet,
# ensuring it is not followed by a newline character.
print("{}".format(output_string), end="")
