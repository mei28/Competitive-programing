n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
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

        return False

    def size(self, x):
        return -self.parents[self.find(x)]


uf = UnionFind(n)

cnt = 0
for a, b in AB:
    uf.union(a - 1, b - 1)


parents = set(filter(lambda x: x >= 0, [uf.find(i) for i in range(n)]))

for p in parents:
    cnt += uf.size(p) * (uf.size(p) - 1) // 2

print(cnt - m)

