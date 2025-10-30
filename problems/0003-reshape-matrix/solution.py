import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    m = len(a)
    n = len(a[0])

    x = new_shape[0]
    y = new_shape[1]

    if m * n != x * y:
        return []


    # np.reshape(a, new_shape)
    o = np.zeros((x, y))

    curr_row = 0
    curr_col = 0

    for i in range(m):
        for j in range(n):
            item = a[i][j]
            if curr_col >= y:
                curr_col = 0
                curr_row += 1
            o[curr_row][curr_col] = item
            curr_col += 1

    return o