import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)


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


n = int(input())
A = []
B = []
S = set()
dct = {}
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    S.add(a)
    S.add(b)
if 1 not in S:
    print(1)
    exit()
S = list(S)
S.sort()

dct = {a: i for i, a in enumerate(S)}
rev_dct = {i: a for i, a in enumerate(S)}

# print(dct)
uf = UnionFind(len(dct))

for a, b in zip(A, B):
    aa = dct[a]
    bb = dct[b]
    uf.union(aa, bb)

# print(uf.members(0))
ans = rev_dct[max(uf.members(0))]
print(ans)
