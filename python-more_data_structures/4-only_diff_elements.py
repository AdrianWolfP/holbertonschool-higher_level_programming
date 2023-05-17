#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniq_set1 = set_1.difference(set_2)
    uniq_set2 = set_2.difference(set_1)
    result = uniq_set1.union(uniq_set2)
    return result
