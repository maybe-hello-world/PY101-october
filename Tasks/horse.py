# horse and chess
move = [[0 for _ in range(8)] for _ in range(8)]
import numpy as np
import timeit

# move = np.array([[0 for _ in range(20)] for _ in range(20)], dtype='int64')


def horse(m,n):
    if m < 0 or n < 0 or m > 7 or n > 7:
    # if m < 0 or n < 0 or m > 19 or n > 19:
        return 0
    if m == 0 and n == 0:
        return 1
    if move[m][n] != 0:
        return move[m][n]
    move[m][n] = horse(m - 2, n - 1) + horse(m + 2, n - 1) + horse(m - 1, n - 2) + horse(m + 1, n - 2)
    return move[m][n]

# print(timeit.timeit(str(horse(19,19)), number = 10)/10)
print(horse(7,7))