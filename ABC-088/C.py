import numpy as np

c = [list(map(int, input().split())) for i in range(3)]

A = np.array(
    [
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1],
    ]
)

B = np.array(
    [
        [1, 0, 0, 1, 0, 0, c[0][0]],
        [1, 0, 0, 0, 1, 0, c[0][1]],
        [1, 0, 0, 0, 0, 1, c[0][2]],
        [0, 1, 0, 1, 0, 0, c[1][0]],
        [0, 1, 0, 0, 1, 0, c[1][1]],
        [0, 1, 0, 0, 0, 1, c[1][2]],
        [0, 0, 1, 1, 0, 0, c[2][0]],
        [0, 0, 1, 0, 1, 0, c[2][1]],
        [0, 0, 1, 0, 0, 1, c[2][2]],
    ]
)

rankA = np.linalg.matrix_rank(A)
rankB = np.linalg.matrix_rank(B)

if rankA == rankB:
    print("Yes")
else:
    print("No")
