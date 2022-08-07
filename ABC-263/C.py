import sys

sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())

ans = []


def dfs(A):
    global ans
    if len(A) == n:
        print(*A)
        return 

    for i in range(A[-1]+1, m + 1):
        A.append(i)
        dfs(A)
        A.pop()


for i in range(1, m+1):
    dfs([i])
