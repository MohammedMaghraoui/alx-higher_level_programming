#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    track = 0
    for x in range(x):
        try:
            if type(my_list[x]) is int:
                print("{:d}".format(my_list[x]), end="")
                track += 1
        except IndexError:
            raise IndexError("list index out of range")
            return track
    print()
    return track
