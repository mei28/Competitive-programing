class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1] * n
        self.n = n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return

    def size(self, x):
        return -self.par[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


n, m, e = map(int, input().split())

edge = []
for i in range(e):
    u, v = map(int, input().split())
    edge.append((u - 1, v - 1))

uf = UnionFind(n + m + 1)
s = n + m

for i in range(n, n + m):
    uf.union(i, s)

con = [1] * e
q = int(input())
X = []
for i in range(q):
    x = int(input())
    x -= 1
    con[x] = 0
    X.append(x)
for i in range(e):
    if con[i]:
        u, v = edge[i]
        uf.union(u, v)

ans = [0] * q

for i in list(range(q))[::-1]:
    ans[i] = uf.size(s) - (m + 1)
    x = X[i]
    u, v = edge[x]
    uf.union(u, v)

print(*ans)
