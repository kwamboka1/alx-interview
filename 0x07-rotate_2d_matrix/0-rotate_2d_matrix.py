#!/usr/bin/python3
""" Module for rotating a matrix function """


def rotate_2d_matrix(matrix):
    """ The function takes a 2D matrix
        and rotates it 90 degree.
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        expected-result = [[7, 4, 1],
                           [8, 5, 2]'
                           [9, 6, 3]]
    """
    n = len(matrix)
    for row in range(0, int(n / 2)):

        for col in range(row, n - row - 1):
            # print((row,col))
            temp = matrix[row][col]

            # print((row,col), (n - 1 - col,row))
            matrix[row][col] = matrix[n - 1 - col][row]

            # print((n - 1 - col,row), (n - 1 - row,n - 1 - col))
            matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]

            # print((n - 1 - row,n - 1 - col), (col,n - 1 - row))
            matrix[n - 1 - row][n - 1 - col] = matrix[col][n - 1 - row]

            # print((col,n - 1 - row))
            matrix[col][n - 1 - row] = temp
