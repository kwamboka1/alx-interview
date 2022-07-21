#!/usr/bin/python3

"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
"""
from sys import argv, exit

def solveNQueens(n):
    """
    A function that places N non-attacking queens on an Nxn chessboard
    """
    posDiag = set() # (r+c)
    negDiag = set() # (r-c)
    col = set()

    result = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        for c in range(n):
            if c in col | (r+c) in posDiag | (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."

    backtrack(0)
    return result
if __name__ == "__main__":

    if len(argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    
        try:
            n = int(argv[1])
        except ValueError:
            print("N must be at least 4")
            exit(1)
        else:
            sol = solveNQueens(n)
            for r in sol:
                print(sol)
