n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * n

    def find(self, x: int):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def issame(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]


uf = UnionFind(n)

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    uf.union(x, y)

sa = [0] * n
sb = [0] * n

for v in range(n):
    r = uf.find(v)
    sa[r] += A[v]
    sb[r] += B[v]

flg = True

for v in range(n):
    r = uf.find(v)
    if sa[r] != sb[r]:
        flg = False

if flg:
    print("Yes")
else:
    print("No")
