import sys

sys.setrecursionlimit(100000)
n = int(input())

edges = []
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges = list(sorted(edges, key=lambda x: x[0]))

parent = [-1] * n


def root(x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = root(parent[x])
        return parent[x]


def unite(x, y):
    x = root(x)
    y = root(y)

    if x > y:
        x, y = y, x
    parent[x] += parent[y]
    parent[y] = x


def size(x):
    x = root(x)
    return -parent[x]


ans = 0
for w, u, v in edges:
    u -= 1
    v -= 1
    ans += w * size(u) * size(v)
    unite(u, v)
print(ans)
