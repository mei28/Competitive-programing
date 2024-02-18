import sys

sys.setrecursionlimit(5000)
n = int(input())

G = [[] for _ in range(n)]

T = []
for i in range(n):
    line = list(map(int, input().split()))
    t = line[0]
    T.append(t)
    k = line[1]
    l = [a - 1 for a in line[2 : 2 + k]]
    G[i] += l


seen = [False] * n
waza = set()


def dfs(G, v):
    seen[v] = True
    waza.add(v)

    for i in G[v]:
        if seen[i]:
            continue
        dfs(G, i)


dfs(G, n - 1)
waza = list(waza)

ans = 0
for i in range(n):
    if i in waza:
        ans += T[i]

print(ans)
