import sys

sys.setrecursionlimit(10**7)
n, m = map(int, input().split())

G = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [False] * n
path = []
answer = 0
limit = 1000000


def dfs(c):
    global answer
    if answer >= limit:
        return
    visited[c] = True
    path.append(c)
    answer += 1

    for d in G[c]:
        if visited[d]:
            continue
        dfs(d)
    visited[c] = False
    path.pop()


dfs(0)
print(answer)
