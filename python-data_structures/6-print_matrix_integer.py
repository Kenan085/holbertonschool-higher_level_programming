#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        lenn = len(matrix[i])
        for j in range(lenn):
            print("{:d}".format(matrix[i][j]), end="")
            if j != lenn - 1:
                print(end=" ")
        print()
