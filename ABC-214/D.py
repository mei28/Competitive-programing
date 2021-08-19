n = int(input())

edgs = []
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    edgs.append((u, v, w))

edgs = list(sorted(edgs, key=lambda x: x[2]))

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
    parent[x] += parent[y]
    parent[y] = x


def size(x):
    x = root(x)
    return -parent[x]


ans = 0

for u, v, w in edgs:
    u -= 1
    v -= 1
    ans += w * size(u) * size(v)
    unite(u, v)
print(ans)
