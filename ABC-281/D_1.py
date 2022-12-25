import sys

sys.setrecursionlimit(10**7)
n, k, d = map(int, input().split())
A = list(map(int, input().split()))
all = set()


def dfs(S):
    global all
    if len(S) >= k:
        all.add(tuple(S))
        return

    for i in range(S[-1] + 1, n):
        S.append(i)
        dfs(S)
        S.pop()


for i in range(n):
    dfs([i])
print(all)
