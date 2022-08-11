import sys

sys.setrecursionlimit(10**8)

MOD = 998244353

n = int(input())

cnt = 0


def dfs(A: str):
    if len(A) == n:
        global cnt
        cnt += 1
        cnt %= MOD
        return

    for di in [-1, 0, 1]:
        if int(A[-1]) == 1 and di == -1:
            continue
        if int(A[-1]) == 9 and di == 1:
            continue

        A += str(int(A[-1]) + di)
        dfs(A)
        A = A[:-1]


for i in range(1, 10):
    dfs(str(i))
print(cnt)
