n, m = map(int, input().split())

ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append((a, b))

par = [i for i in range(n+1)]


def find(x):
    if par[x] == x:
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
        return 0
    par[x] = y


for a, b in ab:
    unite(a, b)

par = par[1:]

se = set()

for i in par:
    se.add(i)

print(len(par)-len(se))