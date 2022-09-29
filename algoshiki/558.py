class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.par = [-1] * n
        self.min_node = [i for i in range(n)]

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
            return False

        if x > y:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x
        self.min_node[x] = min(self.min_node[x], self.min_node[y])

    def get_min_node(self, x):
        return self.min_node[self.root(x)]


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a, b)

for i in range(n):
    print(uf.get_min_node(i))
