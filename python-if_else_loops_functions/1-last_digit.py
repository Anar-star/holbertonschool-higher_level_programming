#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    # This 'else' covers all remaining cases: -10 < last_digit < 6 AND last_digit != 0.
    # The requirement is 'less than 6 and not 0', which is handled by this final condition.
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
