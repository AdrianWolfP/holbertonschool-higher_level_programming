#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for i in my_list:
            if i > max:
                max = 1
        return max
    else:
        return None
