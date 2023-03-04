import sys

sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

G = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

seen = [False] * (n)


def dfs(v):
    seen[v] = True
    for u in G[v]:
        if seen[u]:
            continue
        dfs(u)


dfs(0)

if n - sum(seen) > 0:
    print("No")
else:
    print("Yes")
