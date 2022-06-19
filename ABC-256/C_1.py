import numpy as np

h1, h2, h3, w1, w2, w3 = map(int, input().split())
A = np.array(
    [
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1],
    ]
)
b = np.array([h1, h2, h3, w1, w2, w3])
inv_A = np.linalg.inv(A)
print(inv_A)
