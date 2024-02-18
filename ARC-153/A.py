import sys

sys.setrecursionlimit(10**7)
n = int(input())

candidate = []


def dfs(A):
    if len(A) == 6:
        candidate.append(A)
        return

    for i in range(10):
        A += str(i)
        dfs(A)
        A = A[:-1]


for i in range(1, 10):
    dfs(f"{i}")


can = candidate[n - 1]

print(can[0] + can[0] + can[1] + can[2] + can[3] + can[3] + can[4] + can[5] + can[4])
