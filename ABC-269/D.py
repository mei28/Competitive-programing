from collections import defaultdict


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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(
            f"{r}: {m}" for r, m in self.all_group_members().items()
        )


dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]

mem = [[0] * 2020 for _ in range(2020)]
mer = 1005
n = int(input())
X, Y = [], []
for i in range(n):
    x, y = map(int, input().split())
    x += mer
    y += mer
    X.append(x)
    Y.append(y)
    mem[X[i]][Y[i]] = i

uf = UnionFind(n)

for i in range(n):
    for k in range(6):
        nx = X[i] + dx[k]
        ny = Y[i] + dy[k]

        if mem[nx][ny] > 0:
            uf.union(i, mem[nx][ny])

print(len(uf.all_group_members().keys()))
