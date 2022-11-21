import numpy as np

H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

A_ = np.array(A)
ans = []
masks = []

for i in range(H - h + 1):
    for j in range(W - w + 1):
        mask = np.ones_like(A)
        mask[i : i + h, j : j + w] = 0
        masks.append(mask)
for mask in masks:
    B = A * mask
    B_ = B.reshape(-1)
    ans.append(len(set(list(B_))) - 1)

ans = np.array(ans)
ans = ans.reshape(H - h + 1, -1)
for a in ans:
    print(*a)
