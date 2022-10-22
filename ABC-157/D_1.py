class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

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
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x

        return True

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]


n, m, k = map(int, input().split())
dame = [set() for _ in range(n + 1)]
uf = UnionFind(n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    dame[a].add(b)
    dame[b].add(a)

    uf.union(a, b)


for _ in range(k):
    c, d = map(int, input().split())
    if not uf.is_same(c, d):
        continue
    dame[c].add(d)
    dame[d].add(c)

for i in range(1, n + 1):
    mem = uf.size(i) - 1
    mem -= len(dame[i])
    print(mem)
