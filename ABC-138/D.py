import sys

sys.setrecursionlimit(9000)

n, q = map(int, input().split())
G = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

val = [0] * n

for _ in range(q):
    p, x = map(int, input().split())
    p -= 1
    val[p] += x


def dfs(v: int, p: int, res: list) -> None:
    if p != -1:
        res[v] += res[p]
    for e in G[v]:
        if e == p:
            continue
        dfs(e, v, res)


dfs(0, -1, val)
print(*val)
