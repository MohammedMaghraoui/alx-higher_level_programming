#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

def check_and_print_integer(value):
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

value = 89
check_and_print_integer(value)

value = -89
check_and_print_integer(value)

value = "School"
check_and_print_integer(value)
