#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10

# The task examples show that for negative numbers, the "last digit"
# is the negative value (e.g., -626's last digit is -6).
# The Python modulo operator (%) can return a positive result even for
# negative dividends (e.g., -6 % 10 is 4).
# To align with the task's required output, we adjust the result.
if number < 0 and last_digit != 0:
    last_digit -= 10

message_start = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
    print(f"{message_start} and is greater than 5")
elif last_digit == 0:
    print(f"{message_start} and is 0")
else:
    # This covers cases where the last digit is -1, -2, ..., -9, 1, 2, ..., 5.
    print(f"{message_start} and is less than 6 and not 0")
