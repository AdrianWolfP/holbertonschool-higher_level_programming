#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    myKeys = list(a_dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: a_dictionary[i] for i in myKeys}

    for key in sorted_dict:
        print((key), end='')
        print(":", sorted_dict[key])
