#!/usr/bin/python3
def safe_print_list(my_list, x):
    num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            num += 1
        except IndexError:
            break
    print("")  # Print a newline character after printing the elements
    return num  # Return the number of elements printed

# Example usage:
my_list = [1, 2, 3, 4, 5]
x = 3
printed_count = safe_print_list(my_list, x)
print(f"Printed {printed_count} elements from the list.")
