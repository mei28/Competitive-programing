import sys

sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

G = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

seen = [False] * (n)
gropus = [-1 for _ in range(n)]


def dfs(v):
    seen[v] = True
    for u in G[v]:
        if seen[u]:
            continue
        dfs(u)


ans = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        ans += 1
print(ans)

