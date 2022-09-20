class UnionFind:
    def __init__(self, n, W) -> None:
        self.n = n
        self.par = [-1] * n
        self.weight = W

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
        self.weight[x] += self.weight[y]
        return True

    def get_weight(self, x):
        return self.weight[self.root(x)]


n, m = map(int, input().split())
W = list(map(int, input().split()))
uf = UnionFind(n, W)
for _ in range(m):
    t, x, y = map(int, input().split())
    if t == 0:
        uf.union(x, y)
    else:
        print(uf.get_weight(x))
