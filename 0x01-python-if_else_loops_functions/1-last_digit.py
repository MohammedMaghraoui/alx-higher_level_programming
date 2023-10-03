#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

L_digit = abs(number) % 10
if number < 0:
    L_digit = -L_digit
print("Last digit of {} is {} and is ".format(number, L_digit), end="")

if l_digit > 5:
    print("and is greater than 5")
elif l_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
