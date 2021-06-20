n = int(input())

a = list(map(int, input().split()))

chars = set(a)

parent = [-1] * 220000


def root(x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = root(parent[x])
        return parent[x]


def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    parent[x] += parent[y]
    parent[y] = x


ans = 0

for i in range(n):
    l = i
    r = n - i - 1
    if l < r:
        if root(a[l]) != root(a[r]):
            ans += 1
            unite(a[l], a[r])

print(ans)
