class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1] * n

    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return True

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)


n, m = map(int, input().split())
uf = UnionFind(n)
A = []
for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a, b)


ans = 0

for i in range(n):
    if i == uf.root(i):
        ans += 1
print(ans)
