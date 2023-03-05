import sys

sys.setrecursionlimit(10**7)


def dfs(v):
    global size, edges
    visited[v] = True
    size += 1
    for u in G[v]:
        edges += 1
        if not visited[u]:
            dfs(u)


n, m = map(int, input().split())
G = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [False] * (n)
for v in range(n):
    if not G[v]:
        continue
    if not visited[v]:
        size, edges = 0, 0
        dfs(v)
        if size != edges // 2:
            print("No")
            exit()
print("Yes")
