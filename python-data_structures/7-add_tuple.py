#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = tuple_a[:2] + (0, 0)[len(tuple_a):2]
    b1, b2 = tuple_b[:2] + (0, 0)[len(tuple_b):2]

    sum_1 = a1 + b1
    sum_2 = a2 + b2

    return sum_1, sum_2
