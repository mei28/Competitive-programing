import sys

sys.setrecursionlimit(10**7)
n = int(input())
G = [[] for _ in range(n + 1)]
colors = [-1] * (n + 1)

for _ in range(n - 1):
    u, v, c = map(int, input().split())
    G[u].append((v, c))
    G[v].append((u, c))


def dfs(cv, p, c):
    colors[cv] = c

    for u in G[cv]:
        if u[0] == p:
            continue
        if u[1] % 2 == 0:
            dfs(u[0], cv, c)
        else:
            dfs(u[0], cv, 1 - c)


dfs(1, -1, 0)
print(*colors[1:])
