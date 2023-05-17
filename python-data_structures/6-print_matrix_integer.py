#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    for row in matrix:
        for i, element in enumerate(row):
            if i == cols - 1:
                print("{:d}".format(element), end='')
            else:
                print("{:d}".format(element), end=' ')
        print()
