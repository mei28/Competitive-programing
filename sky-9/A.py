class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.next_index = list(range(n))

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def range_union(self, l, r):
        for i in range(l + 1, r + 1):
            self.union(l, i)


n, q = map(int, input().split())
uf = UnionFind(n)

for _ in range(q):
    t, l, r = map(int, input().split())
    l -= 1
    r -= 1
    if t == 0:
        uf.range_union(l, r)
    else:
        print("Yes" if uf.same(l, r) else "No", end=" ")
