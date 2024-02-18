import sys

sys.setrecursionlimit(10000)
n = int(input())
sx, sy, tx, ty = map(int, input().split())


class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1] * (n)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(len(self.par)) if self.find(i) == root]


points = []
for _ in range(n):
    x, y, r = map(int, input().split())
    points.append([x, y, r])

uf = UnionFind(n)

for i in range(n):
    for j in range(i + 1, n):
        pi = points[i]
        pj = points[j]

        d = (pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2
        if d == (pi[2] + pj[2]) ** 2:
            uf.unite(i, j)
        elif (pi[2] - pj[2]) ** 2 <= d <= (pi[2] + pj[2]) ** 2:
            uf.unite(i, j)
        elif (pi[2] - pj[2]) ** 2 == d:
            uf.unite(i, j)


start = []
goal = []

for i in range(n):
    ix, iy, ir = points[i]

    if (sx - ix) ** 2 + (sy - iy) ** 2 == ir**2:
        start.append(i)

    if (tx - ix) ** 2 + (ty - iy) ** 2 == ir**2:
        goal.append(i)

for x in start:
    for y in goal:
        if uf.same(x, y):
            print("Yes")
            exit()

print("No")
