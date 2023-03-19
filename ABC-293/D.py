n, m = map(int, input().split())


class UnionFind:
    def __init__(self, n) -> None:
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
            return True

        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return False

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())


uf = UnionFind(n)
x, y = 0, 0
for _ in range(m):
    a, b, c, d = input().split()
    a = int(a)
    c = int(c)
    a -= 1
    c -= 1

    if uf.union(a, c):
        y += 1

x = uf.group_count() - y
print(y, x)
