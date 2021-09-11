n, m = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.par = [-1] * (n)

    def root(self, x: int):
        if self.par[x] < 0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def merge(self, x: int, y: int):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x: int, y: int):
        return self.root(x) == self.root(y)

    def size(self, x: int):
        return -self.par[self.root(x)]

A,B =[],[]
for i in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    A.append(a)
    B.append(b)

ans = 0

for i in range(m):
    uf = UnionFind(n)
    for j in range(m):
        if i==j:
            continue
        uf.merge(A[j],B[j])

    num = 0
    for i in range(n):
        if uf.root(i)==i:
            num += 1
    if num>1:
        ans +=1

print(ans)
