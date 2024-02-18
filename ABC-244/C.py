import sys

n = int(input())

P = [False] * (2 * n + 2)
P[0] = True

for i in range(n):
    for idx, j in enumerate(P):
        if j == False:
            print(idx, flush=True)
            P[idx] = True
            break
    k = int(input())
    P[k] = True

for idx, j in enumerate(P):
    if j == False:
        print(idx, flush=True)
        P[idx] = True
        break
