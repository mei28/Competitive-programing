n, q = map(int, input().split())

par = [-1 for _ in range(n + 1)]


def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if par[x] > par[y]:
        x, y = y, x

    par[x] += par[y]
    par[y] = x


for _ in range(q):
    p, a, b = map(int, input().split())

    if p == 0:
        unite(a, b)
    if p == 1:
        if same(a, b):
            print("Yes")
        else:
            print("No")
