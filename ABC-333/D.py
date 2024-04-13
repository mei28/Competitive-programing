from ctypes import wstring_at

n = int(input())


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
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]


uf = UnionFind(n)

for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    if 0 not in [a, b]:
        uf.union(a, b)


ans = [uf.size(i) for i in range(1, n)]
print(max(ans))
